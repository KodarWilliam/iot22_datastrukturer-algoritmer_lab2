from deck import Deck, Card


# Implementera tester ni anser lämpliga här. Motivera gärna varför de behövs (vad de testar och varför).

def test_card_init():
    """Tests that the cards rank and suite are correct after creating a card"""
    card = Card(10, "Clubs")
    assert card.rank == 10
    assert card.suite == "Clubs"

    card = Card(13, "Spades")
    assert card.rank == 13
    assert card.suite == "Spades"


def test_card_compare():
    """Compares ranks of cards, if its equal, lower than or greater than (eq, lt, gt)"""

    """__eq__"""
    card_1 = Card(13, "Hearts")
    card_2 = Card(13, "Spades")
    assert card_1.rank == card_2.rank

    """__lt__"""
    card_1 = Card(1, "Hearts")
    card_2 = Card(11, "Spades")
    assert card_1.rank < card_2.rank

    """__gt__"""
    card_1 = Card(13, "Hearts")
    card_2 = Card(10, "Spades")
    assert card_1.rank > card_2.rank


def test_deck_sort():
    """Tests that the deck is updated after running the methods: shuffle and sort"""
    d = Deck()
    assert d != d.shuffle()  # firstly we make sure that deck is updated after we shuffle it
    assert d != d.sort()  # secondly we make sure deck is updated after we sort it
    assert d.shuffle != d.sort()  # thirdly we make sure the shuffled deck and the sorted deck differ


def test_deck_take():
    """Top card will always be 13 after we sort the deck"""
    d = Deck()
    d.sort()
    assert d.take().rank == 13
    d.take()
    d.take()
    d.take()
    assert d.take().rank == 12  # Here we just make sure that after we took out all 13s from the deck, we should be
    # left with a 12


def test_deck_put():
    """we put Ace of Hearts at top of the deck"""
    """then we take a look at the top card to make sure it got put in"""
    d = Deck()
    d.sort()
    d.put(Card(1, "Hearts"))
    assert d.take().rank == 1 and d.take().suite == "Hearts"
