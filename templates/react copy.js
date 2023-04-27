import React, { useState } from "react";
import "./style.css";

function PlayerStatsForm() 
{
  const [assists, setAssists] = useState("");
  const [boosts, setBoosts] = useState("");
  const [headshotKills, setHeadshotKills] = useState("");
  const [kills, setKills] = useState("");
  const [longestKill, setLongestKill] = useState("");
  const [matchDuration, setMatchDuration] = useState("");
  const [revives, setRevives] = useState("");
  const [teamKills, setTeamKills] = useState("");
  const [vehicleDestroys, setVehicleDestroys] = useState("");
  const [walkDistance, setWalkDistance] = useState("");
  const [weaponsAcquired, setWeaponsAcquired] = useState("");
  const [matchType, setMatchType] = useState("");
  const [results, setResults] = useState("");

  const handleSubmit = async (e) => 
  {
    e.preventDefault();
    const response = await fetch("/predict_datapoint",
     {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ assists, boosts, headshotKills,kills, longestKill, matchDuration, revives, teamKills, vehicleDestroys, walkDistance,weaponsAcquired, matchType }),
     }
    );
    const data = await response.json();
    setResults(data.results);
  };

  return (
    <div className="login">
      <form onSubmit={handleSubmit}>
        <h1>
          <legend>Player Stats</legend>
        </h1>
        <label htmlFor="assists">Assists:</label>
        <input
          type="number"
          id="assists"
          name="assists"
          value={assists}
          onChange={(e) => setAssists(e.target.value)}
        />

        <label htmlFor="boosts">Boosts:</label>
        <input
          type="number"
          id="boosts"
          name="boosts"
          value={boosts}
          onChange={(e) => setBoosts(e.target.value)}
        />
        
        <label htmlFor="boosts">Boosts:</label>
        <input
          type="number"
          id="boosts"
          name="boosts"
          value={boosts}
          onChange={(e) => setBoosts(e.target.value)}
        />

        <label htmlFor="headshotKills">Headshot Kills:</label>
        <input
          type="number"
          id="headshotKills"
          name="headshotKills"
          value={boosts}
          onChange={(e) => setHeadshotKills(e.target.value)}
        />
        <label htmlFor="kills">Kills:</label>
        <input
          type="number"
          id="kills"
          name="kills"
          value={boosts}
          onChange={(e) => setKills(e.target.value)}
        />
        <label htmlFor="boosts">Boosts:</label>
        <input
          type="number"
          id="boosts"
          name="boosts"
          value={boosts}
          onChange={(e) => setBoosts(e.target.value)}
        />
        <label htmlFor="boosts">Boosts:</label>
        <input
          type="number"
          id="boosts"
          name="boosts"
          value={boosts}
          onChange={(e) => setBoosts(e.target.value)}
        />
        <label htmlFor="boosts">Boosts:</label>
        <input
          type="number"
          id="boosts"
          name="boosts"
          value={boosts}
          onChange={(e) => setBoosts(e.target.value)}
        />
        <label htmlFor="boosts">Boosts:</label>
        <input
          type="number"
          id="boosts"
          name="boosts"
          value={boosts}
          onChange={(e) => setBoosts(e.target.value)}
        />
        <label htmlFor="boosts">Boosts:</label>
        <input
          type="number"
          id="boosts"
          name="boosts"
          value={boosts}
          onChange={(e) => setBoosts(e.target.value)}
        />

        <label htmlFor="matchType">Match Type:</label>
        <select
          id="matchType"
          name="matchType"
          value={matchType}
          onChange={(e) => setMatchType(e.target.value)}
          required
        >
          <option value="">--Select a Match Type--</option>
          <option value="squad-fpp">Squad FPP</option>
          <option value="duo-fpp">Duo FPP</option>
          <option value="squad">Squad</option>
          <option value="solo-fpp">Solo FPP</option>
          <option value="duo">Duo</option>
          <option value="solo">Solo</option>
          <option value="normal-squad-fpp">Normal Squad FPP</option>
          <option value="flarefpp">Flare FPP</option>
          <option value="normal-solo-fpp">Normal Solo FPP</option>
          <option value="crashfpp">Crash FPP</option>
          <option value="normal-duo-fpp">Normal Duo FPP</option>
        </select>

        <div className="mb-3">
          <button className="btn btn-primary" type="submit">
            Predict your pubg Score
          </button>
        </div>
      </form>

      {results && (
        <h2>
          The prediction is {results}
        </h2>
      )}
    </div>
  );
}

export default PlayerStatsForm;
