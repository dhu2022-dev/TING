// src/ArtistStats.jsx
import React, { useState } from 'react';
import axios from 'axios';

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
    <div>
      <h1>Artist Stats</h1>
      <input
        type="text"
        value={artistName}
        onChange={(e) => setArtistName(e.target.value)}
        placeholder="Enter artist name"
      />
      <button onClick={fetchArtistStats}>Get Stats</button>

      {loading && <p>Loading...</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}
        
      {artistStats && (
        <div>
          <h2>Spotify Stats</h2>
          <pre>{JSON.stringify(artistStats['Spotify Stats'], null, 2)}</pre>
          <h2>YouTube Stats</h2>
          <pre>{JSON.stringify(artistStats['YouTube Stats'], null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default ArtistStats;