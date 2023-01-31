#blackjack v1
import random

# List of card values
card_values = {'Ace':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10}


# function to calculate the total value of a player's hand
def calculate_hand(hand):
    total = 0
    aces = 0
    for card in hand:
        if card == 'Ace':
            aces += 1
        else:
            total += card_values[card]
    for i in range(aces):
        if total + 11 > 21:
            total += 1
        else:
            total += 11
    return total
    
# function to play again 
def play_again():
  play = input('\nWould you like to play again? Y or N: \n')
  
  if play == 'Y':
      # Create a deck of cards
      deck = list(card_values.keys()) * 4
      random.shuffle(deck)
  
      # Deal initial cards to player and dealer
      player_hand = [deck.pop(), deck.pop()]
      dealer_hand = [deck.pop(), deck.pop()]
  
      # Print initial hands
      print("Player's hand: ", player_hand)
      print("Dealer's hand: ", dealer_hand[0], "and a hidden card")
  
      # Player's turn
      while True:
          choice = input("Do you want to hit or stand? ")
          if choice.lower() == 'hit':
              player_hand.append(deck.pop())
              print("Player's hand: ", player_hand)
              if calculate_hand(player_hand) > 21:
                  print("You bust! You lose.")
                  return
          elif choice.lower() == 'stand':
              break
          else:
              print("Invalid choice. Please enter 'hit' or 'stand'.")
  
      # Dealer's turn
      while calculate_hand(dealer_hand) < 17:
          dealer_hand.append(deck.pop())
      print("Dealer's hand: ", dealer_hand)
  
      # Determine the winner
      player_total = calculate_hand(player_hand)
      dealer_total = calculate_hand(dealer_hand)
      
      if player_total > dealer_total:
          print("You win!")
      elif player_total < dealer_total:
          print("You lose.")
      else:
          print("It's a tie.")
  else: 
    print('Goodbye')

# function to play a game of Blackjack
def play_blackjack():
  print('\nWelcome to Blackjack!\n')
  play = input('Would you like to play? Y or N: \n')
  
  if play == 'Y':
      # Create a deck of cards
      deck = list(card_values.keys()) * 4
      random.shuffle(deck)
  
      # Deal initial cards to player and dealer
      player_hand = [deck.pop(), deck.pop()]
      dealer_hand = [deck.pop(), deck.pop()]
  
      # Print initial hands
      print("\nPlayer's hand: ", player_hand)
      print("\nDealer's hand: ", dealer_hand[0], "and a hidden card")
  
      # Player's turn
      while True:
          choice = input("\nDo you want to hit or stand? \n")
          if choice.lower() == 'hit':
              player_hand.append(deck.pop())
              print("Player's hand: ", player_hand)
              if calculate_hand(player_hand) == 21: 
                print("\nBLACKJACK!!!!!")
                return 
              if calculate_hand(player_hand) > 21:
                  print("\nYou bust! You lose.")
                  play_again()
                  return
          elif choice.lower() == 'stand':
              break
          else:
              print("Invalid choice. Please enter 'hit' or 'stand'.")
  
      # Dealer's turn
      while calculate_hand(dealer_hand) < 17:
          dealer_hand.append(deck.pop())
      print("Dealer's hand: ", dealer_hand)

      while calculate_hand(dealer_hand) > 21:
        print('\nDealer Busted, You Win!')
        return
      while calculate_hand(dealer_hand) == 21:
        print('\nDealer Blackjack!!!! You lost.')
        return
  
      # Determine the winner
      player_total = calculate_hand(player_hand)
      dealer_total = calculate_hand(dealer_hand)
      
      if player_total > dealer_total:
          print("\nYou win!")
          play_again()
      elif player_total < dealer_total:
          print("\nYou lose.")
          play_again()
      else:
          print("\nIt's a tie.")
          play_again()
  else: 
    print('Goodbye')
    
# Run the game
play_blackjack()
