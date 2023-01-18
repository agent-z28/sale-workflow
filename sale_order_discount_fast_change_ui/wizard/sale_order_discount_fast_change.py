from odoo import fields, models


class SaleOrderDiscountFastChange(models.TransientModel):
    _name = "sale.order.discount.fast.change"
    _description = "Sales Order Discount Fast Change"

    discount = fields.Float(string="Discount (%)", digits="Discount", default=0.0)

    def apply_global_discount(self):
        """
        Apply the entered discount to all sale order lines.
        """
        sales_order = self.env["sale.order"].browse(self.env.context.get("active_id"))
        sales_order.order_line.write({"discount": self.discount})
