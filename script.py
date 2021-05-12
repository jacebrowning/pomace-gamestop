import pomace

URL = "https://www.gamestop.com/video-games/xbox-one/games/products/mlb-the-show-21/11116256.html"

settings = pomace.prompt("email")

page = pomace.visit(URL, delay=2)

pomace.log.info("Adding item to card")
page = page.click_add_to_cart(wait=1)
page = page.click_view_cart(delay=1)

pomace.log.info("Proceeding to checkout")
page = page.click_proceed_to_checkout(delay=2)

page.fill_email(settings.email)

page = page.click_guest_checkout()

person = pomace.fake.person
page.fill_first_name(person.first_name)
page.fill_last_name(person.last_name)
page.fill_street_address(person.street_address)

pomace.log.warn("Starting debugger")
breakpoint()
