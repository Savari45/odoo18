/** @odoo-module **/

import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { escape, sprintf } from "@web/core/utils/strings";



export function TestPrintDirect(env,action) {
    console.log('uuuuuuuuuuuuuuuuuuuuuuuuuuuuu',env,action)
    function printPDF(url) {
        var iframe = document.createElement('iframe');
        iframe.src = url;
        iframe.style.display = 'none';
        document.body.appendChild(iframe);
        iframe.onload = function() {
            iframe.contentWindow.print();

        };
        }
        var mess = action.params.text;


        var pdfUrl = mess;

        printPDF(pdfUrl);
        console.log('uuuuuuuuuuuuuuuuuuuuuuuuuuuuu',pdfUrl)


    return
}

registry.category("actions").add("print_direct", TestPrintDirect);
