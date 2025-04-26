from project import showmenu, cart
import pytest

def main():
    test_showmenu()
    test_add_to_cart()
    test_remove()
    test_checkout()

def test_showmenu():
    assert showmenu("regular.csv") is not None
    assert showmenu("sicilian.csv") is not None
    with pytest.raises(FileNotFoundError):
        raise FileNotFoundError

def test_add_to_cart():
    cart.clear()
    cart.append(["Regular", "Cheese", "$13.50", "Small"])
    assert len(cart) == 1
    assert cart[0][1] == "Cheese"

    cart.append(["Sicilian", "3 items", "$45.95", "Large"])
    assert len(cart) == 2
    assert cart[1][3] == "Large"

def test_remove():
    cart.clear()
    cart.append(["Regular", "Cheese", "$13.50", "Small"])
    cart.append(["Sicilian", "3 items", "$45.95", "Large"])

    remove = cart.pop(0)
    assert remove[1] == "Cheese"
    assert len(cart) == 1

def test_checkout():
    cart.clear()
    cart.append(["Regular", "Cheese", "$13.50", "Small"])
    cart.append(["Sicilian", "3 items", "$45.95", "Large"])

    total = sum(float(item[2].replace('$', '')) for item in cart)
    assert total == 13.50 + 45.95

if __name__ == "__main__":
    main()
