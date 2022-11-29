# GALACTIC-HERO 

“Galactic Hero” is a space shooter game using Pygame and Socket Programming. There are 2 characters in the game,

“Lightyear” is the main protagonist. The famed Space Ranger is known for heroism and bravery. Lightyear often suggests that his archenemy Emperor Zurg is behind every evil plot and is often proven correct. He also owns a house on Capital Planet, though, as they all look alike and his duties often keep him away, he is confused over just which one is his.

“Emperor Zurg” is the main antagonist. He is an alien villain action figure and Lightyear’s archenemy. Rules an empire on planet X, and wants to rule the entire universe. Zurg is widely considered the most vicious person in the galaxy, especially with the other villains.

The gameplay is that when Emperor Zurg plots to invade Capital Planet, the home of our hero Lightyear. Lightyear tries to defend his home planet by firing the laser cannon at Zurg.

Two players control different ships. Space Shooter is a fixed shooter in which one of the players moves a laser cannon Vertically across the side of the screen and fires at the opponent overhead.

The goal is to eliminate the opponent before he/she does.


#Implementation

1.The server starts and generates the initial state.
2.As each client connects, they are sent a full copy of the game state.
3.The client takes their turn - their move is sent via a network message to the server.
4.The server makes sure that the move is valid If not, it sends a reply message to the client telling it that their action failed
5. Assuming validation is succeeding, the authoritative game state is modified.
6. New game state is replicated to all clients.
7. When each client gets the new state update, the client re-renders the game UI.

 The nice thing about this type of strategy is that it is hard to cheat since the server validates every move. It is also simple to manage the complexity because the clients never communicate with each other directly at all.
