from pathlib import Path
import re
import shutil


# ============================================================
# 1. Plugins you want to generate
# ============================================================

PLUGINS = [
    {
        "name": "CN",
        "identifier": "com.terry.obsidian.cn",
        "file_name": "CN-2026",
    },
    {
        "name": "US",
        "identifier": "com.terry.obsidian.us",
        "file_name": "US-2026",
    },
    {
        "name": "IN",
        "identifier": "com.terry.obsidian.international",
        "file_name": "International-2026",
    },
    {
        "name": "IV",
        "identifier": "com.terry.obsidian.invest",
        "file_name": "Invest-2026",
    },
    {
        "name": "TD",
        "identifier": "com.terry.obsidian.todo",
        "file_name": "Todo-2026",
    },
     {
        "name": "ST",
        "identifier": "com.terry.obsidian.systemscience",
        "file_name": "ST-2026",
    },
]


# ============================================================
# 2. Global defaults
# ============================================================

VAULT_NAME = "Obsidian"

OUTPUT_DIR = Path.home() / "Desktop" / "PopClip-Obsidian-Plugins"


# ============================================================
# 3. Config.js template
# ============================================================

TEMPLATE = r'''// #popclip
// name: __PLUGIN_NAME__
// identifier: __IDENTIFIER__
// description: Capture plain text to __FILE_NAME__ in Obsidian.
// popclip version: 6221
// app: { name: Obsidian, link: https://obsidian.md/ }
// icon: iconify:simple-icons:obsidian


const options = [
  {
    identifier: "vaultName",
    label: "Vault Name (required)",
    type: "string",
    defaultValue: "__VAULT_NAME__",
    description: "Name of the vault in Obsidian."
  },
  {
    identifier: "fileName",
    label: "File Name",
    type: "string",
    defaultValue: "__FILE_NAME__",
    description: "Optional destination file. Leave blank to use Daily Note."
  },
  {
    identifier: "newFile",
    label: "Always create new file",
    type: "boolean",
    defaultValue: false,
    description: "Create a new file instead of appending."
  },
  {
    identifier: "heading",
    label: "Heading",
    type: "string",
    description: "Optional heading in the target note."
  },
  {
    identifier: "prependDateTime",
    label: "Prepend system datetime",
    type: "boolean",
    defaultValue: true,
    description: "Insert current system date and time at the top."
  },
  {
    identifier: "sourceLink",
    label: "Append source link",
    type: "boolean",
    defaultValue: true,
    description: "Append 'Click here: URL' at the end if a webpage link is available."
  }
];


function cleanText(text) {
  return String(text || "")
    .replace(/\u00A0/g, " ")
    .replace(/\r\n?/g, "\n")
    .replace(/[ \t]+$/gm, "")
    .replace(/\n{2,}/g, "\n")
    .trim();
}


function safeEncode(value) {
  var text = String(value == null ? "" : value)
    .replace(/\u0000/g, "");

  try {
    if (typeof text.normalize === "function") {
      text = text.normalize("NFC");
    }
  } catch (e) {
    // Keep original text if normalization fails.
  }

  try {
    return encodeURIComponent(text);
  } catch (e) {
    text = text.replace(
      /[\uD800-\uDFFF]/g,
      "\uFFFD"
    );

    return encodeURIComponent(text);
  }
}


function encodeDataForAdvancedUri(text) {
  var cleaned = String(
    text == null ? "" : text
  ).replace(/\u0000/g, "");

  try {
    if (typeof cleaned.normalize === "function") {
      cleaned = cleaned.normalize("NFC");
    }
  } catch (e) {
    // Keep original text if normalization fails.
  }

  try {
    return encodeURIComponent(
      encodeURIComponent(cleaned)
    );
  } catch (e) {
    cleaned = cleaned.replace(
      /[\uD800-\uDFFF]/g,
      "\uFFFD"
    );

    return encodeURIComponent(
      encodeURIComponent(cleaned)
    );
  }
}


function pad2(value) {
  return value < 10
    ? "0" + value
    : String(value);
}


function formatSystemDateTime() {
  var now = new Date();

  var year = now.getFullYear();
  var month = now.getMonth();
  var day = now.getDate();
  var hour = now.getHours();
  var minute = now.getMinutes();

  var monthNames = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
  ];

  return (
    monthNames[month] +
    " " +
    day +
    ", " +
    year +
    " " +
    pad2(hour) +
    ":" +
    pad2(minute)
  );
}


function buildObsidianUrl(options, text) {
  var params = [];

  params.push(
    "vault=" +
    safeEncode(options.vaultName || "")
  );

  if (options.fileName) {
    params.push(
      "filename=" +
      safeEncode(options.fileName)
    );
  } else {
    params.push("daily=true");
  }

  if (options.heading) {
    params.push(
      "heading=" +
      safeEncode(options.heading)
    );
  }

  params.push(
    "data=" +
    encodeDataForAdvancedUri(text)
  );

  params.push(
    "mode=" +
    safeEncode(
      options.newFile
        ? "new"
        : "append"
    )
  );

  return (
    "obsidian://advanced-uri?" +
    params.join("&")
  );
}


function capture(text, options) {
  text = cleanText(text);

  if (!text) {
    return;
  }

  var url = buildObsidianUrl(
    options,
    text
  );

  return popclip.openUrl(
    url,
    { activate: false }
  );
}


defineExtension({
  options: options,

  action: {
    captureHtml: false,

    code: async function (
      input,
      options,
      context
    ) {
      try {
        var content = cleanText(
          input.text || ""
        );

        if (!content) {
          return;
        }

        if (options.prependDateTime) {
          content =
            "<br>" +
            formatSystemDateTime() +
            "\n" +
            content;
        }

        if (
          options.sourceLink &&
          context &&
          context.browserUrl
        ) {
          content +=
            "\nClick here: " +
            context.browserUrl;
        }

        if (!options.newFile) {
          content =
            "\n" +
            content;
        }

        await capture(
          content,
          options
        );

      } catch (error) {
        popclip.showText(
          "Obsidian error: " +
          String(
            error &&
            error.message
              ? error.message
              : error
          )
        );
      }
    }
  }
});
'''


# ============================================================
# 4. Helpers
# ============================================================

def safe_folder_name(name):
    """
    Convert the plugin display name into a safe macOS folder name.
    """
    name = re.sub(r'[/:]', '-', name)
    name = re.sub(r'\s+', ' ', name).strip()

    return name


def validate_plugins():
    """
    Prevent duplicate identifiers.
    """
    identifiers = set()

    for plugin in PLUGINS:
        identifier = plugin["identifier"]

        if identifier in identifiers:
            raise ValueError(
                f"Duplicate identifier: {identifier}"
            )

        identifiers.add(identifier)


def build_config(plugin):
    """
    Generate Config.js for one plugin.
    """
    config = TEMPLATE

    replacements = {
        "__PLUGIN_NAME__": plugin["name"],
        "__IDENTIFIER__": plugin["identifier"],
        "__FILE_NAME__": plugin["file_name"],
        "__VAULT_NAME__": VAULT_NAME,
    }

    for old, new in replacements.items():
        config = config.replace(
            old,
            str(new)
        )

    return config


def generate_plugin(plugin):
    """
    Generate one .popclipext package.
    """
    folder_name = (
        safe_folder_name(plugin["name"])
        + ".popclipext"
    )

    package_path = OUTPUT_DIR / folder_name

    if package_path.exists():
        shutil.rmtree(package_path)

    package_path.mkdir(
        parents=True,
        exist_ok=True
    )

    config_path = (
        package_path /
        "Config.js"
    )

    config_path.write_text(
        build_config(plugin),
        encoding="utf-8"
    )

    return package_path


# ============================================================
# 5. Generate all plugins
# ============================================================

def main():
    validate_plugins()

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    print()
    print("Generating PopClip plugins...")
    print()

    for plugin in PLUGINS:
        path = generate_plugin(plugin)

        print(
            f"✓ {plugin['name']}"
        )

        print(
            f"  → {plugin['file_name']}"
        )

        print(
            f"  → {plugin['identifier']}"
        )

        print(
            f"  → {path}"
        )

        print()

    print(
        f"Done. Generated {len(PLUGINS)} plugins."
    )

    print(
        f"Output: {OUTPUT_DIR}"
    )


if __name__ == "__main__":
    main()