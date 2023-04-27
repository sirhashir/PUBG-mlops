import React, { useState } from "react";
import "./style.css";

function PlayerStatsForm() 
{
  const [data, setData] = useState({
    assists:"",
    boosts:"",
    headshotKills:"",
    kills:"",
    longestKill:"",
    matchDuration:"",
    revives:"",
    teamKills:"",
    vehicleDestroys:"",
    walkDistance:"",
    weaponsAcquired:"",
    matchType:"",
    results:""
  })
  // const [assists, setAssists] = useState("");
  // const [boosts, setBoosts] = useState("");
  // const [headshotKills, setHeadshotKills] = useState("");
  // const [kills, setKills] = useState("");
  // const [longestKill, setLongestKill] = useState("");
  // const [matchDuration, setMatchDuration] = useState("");
  // const [revives, setRevives] = useState("");
  // const [teamKills, setTeamKills] = useState("");
  // const [vehicleDestroys, setVehicleDestroys] = useState("");
  // const [walkDistance, setWalkDistance] = useState("");
  // const [weaponsAcquired, setWeaponsAcquired] = useState("");
  // const [matchType, setMatchType] = useState("");
  // const [results, setResults] = useState("");

  const handleSubmit = async (e) => 
  {
    e.preventDefault();
    const response = await fetch("/predict_datapoint",
     {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
     }
    );
    const data = await response.json();
    setResults(data.results);
  };

  return (
    <div className="">
      <form onSubmit={handleSubmit}>
        <h1>
          <legend>Player Stats</legend>
        </h1>
        <label htmlFor="assists">Assists:</label>
        <input
          type="number"
          id="assists"
          name="assists"
          value={data.assists}
          onChange={(e) => setData({...data, assists:e.target.value})}
        />
        
        <label htmlFor="boosts">Boosts:</label>
        <input
          type="number"
          id="boosts"
          name="boosts"
          value={data.boosts}
          onChange={(e) => setData({...data, boosts:e.target.value})}
        />

        <label htmlFor="headshotKills">Headshot Kills:</label>
        <input
          type="number"
          id="headshotKills"
          name="headshotKills"
          value={data.headshotKills}
          onChange={(e) => setData({...data, headshotKills:e.target.value})}
        />

        <label htmlFor="kills">Kills:</label>
        <input
          type="number"
          id="kills"
          name="kills"
          value={data.kills}
          onChange={(e) => setData({...data, kills:e.target.value})}
        />

        <label htmlFor="longestKill">Longest Kill:</label>
        <input
          type="number"
          id="longestKill"
          name="longestKill"
          value={data.longestKill}
          onChange={(e) => setData({...data, longestKill:e.target.value})}
        />

        <label htmlFor="matchDuration">Match Duration:</label>
        <input
          type="number"
          id="matchDuration"
          name="matchDuration"
          value={data.matchDuration}
          onChange={(e) => setData({...data, matchDuration:e.target.value})}
        />
        <label htmlFor="revives">Revives:</label>
        <input
          type="number"
          id="revives"
          name="revives"
          value={data.revives}
          onChange={(e) => setData({...data, revives:e.target.value})}
        />

        <label htmlFor="teamKills">Team Kills:</label>
        <input
          type="number"
          id="teamKills"
          name="teamKills"
          value={data.teamKills}
          onChange={(e) => setData({...data, teamKills:e.target.value})}
        />

        <label htmlFor="vehicleDestroys">Vehicle Destroys:</label>
        <input
          type="number"
          id="vehicleDestroys"
          name="vehicleDestroys"
          value={data.vehicleDestroys}
          onChange={(e) => setData({...data, vehicleDestroys:e.target.value})}
        />

        <label htmlFor="walkDistance">Walk Distance:</label>
        <input
          type="number"
          id="walkDistance"
          name="walkDistance"
          value={data.walkDistance}
          onChange={(e) => setData({...data, walkDistance:e.target.value})}
        />

        <label htmlFor="weaponsAcquired">Weapons Acquired:</label>
        <input
          type="number"
          id="weaponsAcquired"
          name="weaponsAcquired"
          value={data.weaponsAcquired}
          onChange={(e) => setData({...data, weaponsAcquired:e.target.value})}
        />

        <label htmlFor="matchType">Match Type:</label>
        <select
          id="matchType"
          name="matchType"
          value={data.matchType}
          onChange={(e) => setData({...data, matchType:e.target.value})}
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
