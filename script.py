import pomace

URL = "https://www.gamestop.com/video-games/xbox-one/games/products/mlb-the-show-21/11116256.html"

settings = pomace.prompt("email")

page = pomace.visit(URL, delay=2)
page = page.click_add_to_cart(wait=1)
page = page.click_view_cart(delay=1)
page = page.click_proceed_to_checkout(delay=2)

page.fill_email(settings.email)

breakpoint()
