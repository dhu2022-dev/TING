import React, { useState } from 'react';
import axios from 'axios';
import ArtistCard from './artist_card'; // Import the new component
import RelatedArtistCard from "./related_artist_card"
import '../styles/app.css'

const ArtistStats = () => {
  const [artistName, setArtistName] = useState('');
  const [artistStats, setArtistStats] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const fetchArtistStats = async () => {
    if (!artistName) {
      setError('Please enter an artist name.');
      return;
    }
    setLoading(true);
    setError('');
    try {
      const response = await axios.get(`/api/artists?artist_name=${artistName}`);
      setArtistStats(response.data);
    } catch (err) {
      setError('Failed to fetch artist stats. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div class = "overall-background">
      <div class = 'form-container'>
        <h1>Artist Stats</h1>
        <br></br>
        <input
          type="text"
          value={artistName}
          onChange={(e) => setArtistName(e.target.value)}
          placeholder="Enter artist name"
        />
        <button onClick={fetchArtistStats}>Get Stats</button>

        {loading && <p>Loading...</p>}
        {error && <p style={{ color: 'red' }}>{error}</p>}
      </div>
      {/* {artistStats && (
        <div>
          <h2>Spotify Stats</h2>
          <pre>{JSON.stringify(artistStats['Spotify Stats'], null, 2)}</pre>
          <h2>YouTube Stats</h2>
          <pre>{JSON.stringify(artistStats['YouTube Stats'], null, 2)}</pre>
        </div>
      )} */}
  
      {artistStats && (
        <>
        <ArtistCard artist_spotify={artistStats['Spotify Stats']} artist_youtube={artistStats['YouTube Stats']} />
        
        <h2 class = "title">Similar Artists</h2>
        <div className="similar-artists-container">
          {artistStats["Spotify Stats"].related_artists.artists.map((artist, index) => (
            <RelatedArtistCard 
              key={index}
              artist_spotify={artist} // Pass the current artist data to the card
            />
          ))}
        </div>
        </>
      )}
    </div>
  );
};

export default ArtistStats;