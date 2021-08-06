
import * as React from 'react';
import './review.css';


const list = [
    {
      collectionName: 'Jumanji: Welcome to the Jungle + Jumanji: The Next Level',
      collectionViewUrl: 'https://reactjs.org/',
      artistName: 'Jordan Walke',
      primaryGenreName: "Action",
      collectionId: 1502169871,
    },
  ];
  
  const music = [
    {
      artistName: 'Jack Johnson',
      artistLinkUrl: 'https://music.apple.com/us/artist/jack-johnson/909253?uo=4',
      primaryGenreName: "Rock",
      artistId: 909253,
      artistType: "Artist",
    }

  ]

  const Review = () => (
    <ul>
      {list.map((item) => (
        <li key={item.collectionId}>
          <span>
              <h1 className="review"><strong></strong> {item.collectionName}</h1>
            <a href={item.artistLinkUrl}></a>
          </span>
          <br/>
          <span><strong>Director: </strong>{item.artistName}</span>
          <br />
          <span><strong>Genre: </strong>{item.primaryGenreName}</span>
          <br />
          <span><strong>Summary: </strong> Five kids are forced to fight for their lives in 
          the jungle after being sucked into a video game</span>
          <br />
          <span><strong>Cast: </strong> The Rock and other people</span>
          <br />
          <span><strong>Review: </strong> Its ok</span>
          <br />
        </li>
      ))}
    </ul>
  );
  

  export default Review;
