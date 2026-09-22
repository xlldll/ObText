// #popclip
// name: Minimal Module Snippet
defineExtension({
  action: () => popclip.showText("hi friends!")
});

// exports.options = [
//   {
//     identifier: "vaultName",
//     label: "Vault Name (required)",
//     type: "string",
//     defaultValue: "Obsidian",
//     description: "Name of the vault in Obsidian."
//   },
//   {
//     identifier: "fileName",
//     label: "File Name",
//     type: "string",
//     defaultValue: "Test",
//     description: "Optional destination file. Leave blank to use Daily Note."
//   },
//   {
//     identifier: "newFile",
//     label: "Always create new file",
//     type: "boolean",
//     defaultValue: false,
//     description: "Create a new file instead of appending."
//   },
//   {
//     identifier: "heading",
//     label: "Heading",
//     type: "string",
//     description: "Optional heading in the target note."
//   },
//   {
//     identifier: "prependDateTime",
//     label: "Prepend system datetime",
//     type: "boolean",
//     defaultValue: true,
//     description: "Insert current system date and time at the top."
//   },
//   {
//     identifier: "sourceLink",
//     label: "Append source link",
//     type: "boolean",
//     defaultValue: true,
//     description: "Append 'Click here: URL' at the end if a webpage link is available."
//   }
// ];

// function cleanText(text) {
//   return String(text || "")
//     .replace(/\u00A0/g, " ")        // replace non-breaking space
//     .replace(/\r\n?/g, "\n")        // normalize line breaks
//     .replace(/[ \t]+$/gm, "")       // remove trailing spaces
//     .replace(/\n{2,}/g, "\n")       // collapse ALL blank lines to ONE line
//     .trim();                        // remove leading/trailing blank lines
// }

// function safeEncode(value) {
//   var text = String(value == null ? "" : value)
//     .replace(/\u0000/g, "")
//     .normalize("NFC");

//   try {
//     return encodeURIComponent(text);
//   } catch (e) {
//     text = text.replace(/[\uD800-\uDFFF]/g, "\uFFFD");
//     return encodeURIComponent(text);
//   }
// }


// function formatSystemDateTime() {
//   var now = new Date();

//   var year = now.getFullYear();
//   var month = now.getMonth();
//   var day = now.getDate();
//   var hour = now.getHours();
//   var minute = now.getMinutes();

//   var monthNames = [
//     "January",
//     "February",
//     "March",
//     "April",
//     "May",
//     "June",
//     "July",
//     "August",
//     "September",
//     "October",
//     "November",
//     "December"
//   ];

//   var monthName = monthNames[month];
//   var hourText = String(hour).padStart(2, "0");
//   var minuteText = String(minute).padStart(2, "0");

//   return monthName + " " + day + ", " + year + " " + hourText + ":" + minuteText;
// }

// function buildObsidianUrl(options, text) {
//   var params = [];

//   params.push("vault=" + safeEncode(options.vaultName || ""));

//   if (options.fileName) {
//     params.push("filename=" + safeEncode(options.fileName));
//   } else {
//     params.push("daily=true");
//   }

//   if (options.heading) {
//     params.push("heading=" + safeEncode(options.heading));
//   }

//   params.push("data=" + safeEncode(text));
//   params.push("mode=" + safeEncode(options.newFile ? "new" : "append"));

//   return "obsidian://advanced-uri?" + params.join("&");
// }

// function capture(text, options) {
//   text = cleanText(text);

//   if (!text) {
//     return;
//   }

//   var url = buildObsidianUrl(options, text);
//   // var url = "obsidian://advanced-uri?vault=Obsidian&filename=Test&data=%253Cbr%253ESeptember%252022%252C%25202026%252011%253A43%250AHello%2520World&mode=append";
//   // url = "obsidian://advanced-uri?vault=Obsidian&filename=Test&data=Hello&mode=append"
//   // popclip.openUrl(url1, { activate: false });
//   // popclip.copyText(url1);
//   // popclip.openUrl(url, { activate: false });
//   popclip.copyText(url);

// }

// exports.action = {
//   captureHtml: false,
//   code: function (input, options, context) {
//     popclip.copyText("STEP 1 OK");
//   }
//   // code: function (input, options, context) {
//   //   var raw = input.text || "";

//   //   var content = cleanText(raw);

//   //   if (!content) {
//   //     return;
//   //   }

//   //   if (options.prependDateTime) {
//   //     content = "<br>" + formatSystemDateTime() + "\n" + content;
//   //   }

//   //   if (options.sourceLink && context && context.browserUrl) {
//   //     content = content + "\nClick here: " + context.browserUrl;
//   //   }


//   //   if (!options.newFile) {
//   //     content = "\n" + content;
//   //   }

//   //   capture(content, options);
//   // }
// };

