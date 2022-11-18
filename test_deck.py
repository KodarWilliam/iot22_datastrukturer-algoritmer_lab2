from deck import Deck, Card


# Implementera tester ni anser lämpliga här. Motivera gärna varför de behövs (vad de testar och varför).

def test_card():
    """Tests that the cards rank and suite are correct"""
    card = Card(10, "Clubs")
    assert card.rank == 10
    assert card.suite == "Clubs"

    card = Card(13, "Spades")
    assert card.rank == 13
    assert card.suite == "Spades"


def test_deck():
    """Tests that the deck is updated after running the methods: shuffle and sort"""
    d = Deck()
    assert d != d.shuffle()
    assert d != d.sort()
    assert d.shuffle != d.sort()
