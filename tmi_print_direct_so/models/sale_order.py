# -*- coding: utf-8 -*-
###################################################################################
#
#    Copyright (c) 2023 tmistones.com
#
#
#
#
###################################################################################


from odoo import api, fields, models, tools
from odoo.exceptions import UserError, AccessError


from datetime import datetime

import logging
_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):

    _inherit = ['sale.order']

    def print_direct(self):

        domain_attch = [('name','like','tmi_print_direct_so_')]
        Attachs = self.env['ir.attachment'].sudo().search (domain_attch)

        if Attachs:
            for Attach in Attachs:
                Attach.sudo().unlink()
                #_logger.info("The Attach are: %r", Attach.name)


        Report_model = self.env['ir.actions.report'].sudo()
        report_ref = 'sale.action_report_saleorder'


        report_sudo = Report_model._get_report_from_name(report_ref)
        report_template = Report_model.browse([self.env.ref(report_ref).id])

        report_content = report_template._render_qweb_pdf('sale.action_report_saleorder',res_ids=self.id)

        now = datetime.now()

        attachment_name = 'tmi_print_direct_so_'+now.strftime("%H_%M_%S")

        attachment_vals_list = []

        attachment_vals_list.append({
            'name': attachment_name,
            'raw': report_content[0],
            'res_model': report_sudo.model,
            'res_id': self.id,
            'type': 'binary',
            'public': True,
        })
        temp_attachment = self.env['ir.attachment'].create(attachment_vals_list)
        #
        # try:
        #     temp_attachment = self.env['ir.attachment'].create(attachment_vals_list)
        #
        # except AccessError:
        #     _logger.info("Cannot save temporary PDF report %r attachments for user %r", attachment_name,
        #                  self.env.user.display_name)
        # else:
        #     _logger.info("The temporary PDF documents %r are now saved in the database", attachment_name)
        #    # _logger.info("The PDF public status: %r", temp_attachment.public)
        #     #_logger.info("The PDF local_url: %r", temp_attachment.local_url)
        #
        # #_logger.info("The PDF report has been: records %s.", report_sudo)

        return {
            'type': 'ir.actions.client',
            'tag': 'print_direct',
            'params': {
                'text': temp_attachment.local_url
            }
        }

    def print_direct_pro_forma(self):
        domain_attch = [('name', 'like', 'tmi_print_direct_so_pro-forma_')]
        Attachs = self.env['ir.attachment'].sudo().search(domain_attch)

        if Attachs:
            for Attach in Attachs:
                Attach.sudo().unlink()
                # _logger.info("The Attach are: %r", Attach.name)

        Report_model = self.env['ir.actions.report'].sudo()
        report_ref = 'sale.action_report_pro_forma_invoice'
        report_sudo = Report_model._get_report(report_ref)
        report_content = Report_model._render_qweb_pdf(report_ref, res_ids=self.id)

        now = datetime.now()

        attachment_name = 'tmi_print_direct_so_pro-forma_' + now.strftime("%H_%M_%S")

        attachment_vals_list = []

        attachment_vals_list.append({
            'name': attachment_name,
            'raw': report_content[0],
            'res_model': report_sudo.model,
            'res_id': self.id,
            'type': 'binary',
            'public': True,
        })

        try:
            temp_attachment = self.env['ir.attachment'].create(attachment_vals_list)

        except AccessError:
            _logger.info("Cannot save temporary PDF report %r attachments for user %r", attachment_name,
                         self.env.user.display_name)
        else:
            _logger.info("The temporary PDF documents %r are now saved in the database", attachment_name)
        # _logger.info("The PDF public status: %r", temp_attachment.public)
        # _logger.info("The PDF local_url: %r", temp_attachment.local_url)

        # _logger.info("The PDF report has been: records %s.", report_sudo)

        return {
            'type': 'ir.actions.client',
            'tag': 'print_direct',
            'params': {
                'text': temp_attachment.local_url
            }
        }