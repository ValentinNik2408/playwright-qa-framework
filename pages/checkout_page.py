from playwright.sync_api import Page, expect

class CheckoutPage:
    def correct_items_added(self, page, first_item, second_item): #TODO make it for more than two items
        table = page.locator(".table")
        expect(table).to_be_visible()
        rows = table.locator("tr")
        expect(rows).to_have_count(4)
        columns = rows.locator("th")
        expect(columns).to_have_count(5)
        all_rows_data = rows.all()
        added_items_in_cart = []

        for row in all_rows_data[1:-1]:
            item_title = row.locator("td").nth(0).inner_text()
            clean_item_title=item_title.replace('\xa0', '').strip()
            added_items_in_cart.append(clean_item_title)
        print(added_items_in_cart)
        assert(added_items_in_cart[0]) == first_item
        assert(added_items_in_cart[1]) == second_item

    def calculate_total_price(self, page, total_price_expectation): #TODO make all variables global
        table = page.locator(".table")
        expect(table).to_be_visible()
        rows = table.locator("tr")
        expect(rows).to_have_count(4)
        columns = rows.locator("th")
        expect(columns).to_have_count(5)
        all_rows_data = rows.all()
        total_price = 0
        
        for data in all_rows_data[1:-1]:
            price = data.locator("td").nth(3).inner_text()
            clean_price=price.replace('$', '')
            total_price += float(clean_price)
        print("Total price is:",total_price)
        assert(total_price) == total_price_expectation                
