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
            <a href={item.artistLinkUrl}> <strong>Title: </strong> {item.collectionName}</a>
          </span>
          <br/>
          <span><strong>Director: </strong>{item.artistName}</span>
          <br />
          <span><strong>Genre: </strong>{item.primaryGenreName}</span>
          <br />
        </li>
      ))}
    </ul>
  );
  

  export default Review;
