import React from 'react';
import Card from 'react-bootstrap/Card';
import ListGroup from 'react-bootstrap/ListGroup';
import '../styles/app.css';

const ArtistCard = ({ artist_spotify, artist_youtube }) => {
  const { name, images, followers, genres, popularity, external_urls } = artist_spotify;
  const { items } = artist_youtube;
  
  // Assuming subscriberCount is part of the statistics object
  const youtubeSubscribers = items[0].statistics.subscriberCount;

  return (
    <div className="card-container">
        <Card style={{ width: '18rem' }}>
        <Card.Img variant="top" src={images[1].url} className="card-img-top"/>
        <Card.Body className="card-body">
            <Card.Title>{name}</Card.Title>
            <Card.Text>
                <strong>Spotify Followers:</strong> {followers.total.toLocaleString()}
            </Card.Text>
            <Card.Text>
                <strong>Spotify Popularity:</strong> {popularity}
            </Card.Text>
            <Card.Text>
                <strong>YouTube Subscribers:</strong> {youtubeSubscribers ? youtubeSubscribers.toLocaleString() : "N/A"}
            </Card.Text>
            <ListGroup variant="flush">
            <ListGroup.Item><strong>Genres:</strong> {genres.join(', ')}</ListGroup.Item>
            </ListGroup>
            <Card.Link href={external_urls.spotify} target="_blank">Open in Spotify</Card.Link>
        </Card.Body>
        </Card>
    </div>
  );
};

export default ArtistCard;