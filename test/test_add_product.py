def test_add_product(app):
    app.home.open_home_page()
    app.home.add_item_to_the_basket()
    app.home.add_item_to_the_basket()
    app.home.add_item_to_the_basket()
    app.basket.remove_items()


