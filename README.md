# Setup

```
brew install pipx

git clone https://github.com/jacebrowning/pomace-gamestop
cd pomace-gamestop
```

# Interactive

```
pipx run pomace run https://www.gamestop.com/video-games/xbox-one/games/products/mlb-the-show-21/11116256.html
```

- click_add_to_cart
- click_view_card
- click_proceed_to_checkout
- fill_email

# Scripted

```
pipx run --spec=pomace==0.8b2 pomace exec script.py
```
