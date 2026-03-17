// #popclip
// name: Obsidian Plain Text Safe
// identifier: com.example.obsidian.plaintextsafe
// description: Capture plain text to Obsidian with strict escaping and system datetime.
// popclip version: 4688
// app: { name: Obsidian, link: https://obsidian.md/ }
// icon: iconify:simple-icons:obsidian

exports.options = [
  {
    identifier: "vaultName",
    label: "Vault Name (required)",
    type: "string",
    defaultValue: "Obsidian",
    description: "Name of the vault in Obsidian."
  },
  {
    identifier: "fileName",
    label: "File Name",
    type: "string",
    defaultValue: "CN-2026",
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
    .replace(/\n{3,}/g, "\n\n")
    .trim();
}

function safeEncode(value) {
  var text = String(value == null ? "" : value)
    .replace(/\u0000/g, "")
    .normalize("NFC");

  try {
    return encodeURIComponent(text);
  } catch (e) {
    text = text.replace(/[\uD800-\uDFFF]/g, "\uFFFD");
    return encodeURIComponent(text);
  }
}

function encodeDataForAdvancedUri(text) {
  var cleaned = String(text == null ? "" : text)
    .replace(/\u0000/g, "")
    .normalize("NFC");

  try {
    return encodeURIComponent(encodeURIComponent(cleaned));
  } catch (e) {
    cleaned = cleaned.replace(/[\uD800-\uDFFF]/g, "\uFFFD");
    return encodeURIComponent(encodeURIComponent(cleaned));
  }
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

  var monthName = monthNames[month];
  var hourText = String(hour).padStart(2, "0");
  var minuteText = String(minute).padStart(2, "0");

  return monthName + " " + day + ", " + year + " " + hourText + ":" + minuteText;
}

function buildObsidianUrl(options, text) {
  var params = [];

  params.push("vault=" + safeEncode(options.vaultName || ""));

  if (options.fileName) {
    params.push("filename=" + safeEncode(options.fileName));
  } else {
    params.push("daily=true");
  }

  if (options.heading) {
    params.push("heading=" + safeEncode(options.heading));
  }

  params.push("data=" + encodeDataForAdvancedUri(text));
  params.push("mode=" + safeEncode(options.newFile ? "new" : "append"));

  return "obsidian://advanced-uri?" + params.join("&");
}

function capture(text, options) {
  text = cleanText(text);

  if (!text) {
    return;
  }

  var url = buildObsidianUrl(options, text);
  popclip.openUrl(url, { activate: false });
}

exports.action = {
  captureHtml: false,
  code: function (input, options, context) {
    var raw = input.text || "";
    var content = cleanText(raw);

    if (!content) {
      return;
    }

    if (options.prependDateTime) {
      content = "<br>" + formatSystemDateTime() + "\n" + content;
    }

    if (options.sourceLink && context && context.browserUrl) {
      content = content + "\nClick here: " + context.browserUrl;
    }

    if (!options.newFile) {
      content = "\n" + content;
    }

    capture(content, options);
  }
};