import { useState } from "react";
import axios from 'axios'

const TestFormm = () => {
  const [data, setData] = useState({
    assists: "",
    boosts: "",
    headshotKills: "",
    kills: "",
    longestKill: "",
    matchDuration: "",
    revives: "",
    teamKills: "",
    vehicleDestroys: "",
    walkDistance: "",
    weaponsAcquired: "",
    matchType: "",
  });
  const [results, setResults] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    await axios.post("http://127.0.0.1:5000/predictdata", {
        Headers:{
            "Content-Type": "application/json",
            "cors": "no-cors",
            "data": data
        }
    }, data)
    .then((res) => {
       window.alert(res.data);
    })
    .catch(err => console.log(err))
  };
  return (
    <div>
      <div className="container-fluid">
        {/* <div className='row'>
            <div className='col-8 bg-success h-25'>hy</div>
            <div className='col-3 bg-danger h-25'>hello</div>
            <div className='col-1 bg-secondary'>hey</div>
        </div> */}
        <div className="row justify-content-center">
          <div className="col-12">
            <div className="card d-flex mx-auto my-5">
              <div className="row">
                <div className="col-md-5 col-12 c1 p-5">
                  <div className="row mb-5 m-3">
                    {" "}
                    <img
                      src="https://i.imgur.com/pFfTOwy.jpg"
                      width="70vw"
                      height="55vh"
                      alt=""
                    />{" "}
                  </div>{" "}
                  <img
                    src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTh0cOvKAMLzitAHKOoiECLh5bmwiid_AKJhazc8aV9cg&s"
                    // width="120vw"
                    // height="210vh"
                    className="mx-auto d-flex"
                    alt="Teacher"
                  />
                  <div className="row justify-content-center">
                    <div className="w-75 mx-md-5 mx-1 mx-sm-2 mb-5 mt-4 px-sm-5 px-md-2 px-xl-1 px-2">
                      <h1 className="wlcm">Welcome to your Predictor</h1>{" "}
                      <span className="sp1">
                        {" "}
                        <span className="px-3 bg-danger rounded-pill"></span>{" "}
                        <span className="ml-2 px-1 rounded-circle"></span>{" "}
                        <span className="ml-2 px-1 rounded-circle"></span>{" "}
                      </span>
                    </div>
                  </div>
                </div>
                <div className="col-md-3 col-12 c2 px-5 pt-5">
                  <div className="row justify-content-center"></div>
                  <form onSubmit={handleSubmit}>
                    <h1>
                      <legend>Player Stats</legend>
                    </h1>
                    <div className="row">
                      <label htmlFor="assists">Assists:</label>
                      <input
                        type="number"
                        id="assists"
                        name="assists"
                        value={data.assists}
                        onChange={(e) =>
                          setData({ ...data, assists: e.target.value })
                        }
                      />
                    </div>
                    <div className="row">
                      <label htmlFor="boosts">Boosts:</label>
                      <input
                        type="number"
                        id="boosts"
                        name="boosts"
                        value={data.boosts}
                        onChange={(e) =>
                          setData({ ...data, boosts: e.target.value })
                        }
                      />
                    </div>
                    <div className="row">
                      <label htmlFor="headshotKills">Headshot Kills:</label>
                      <input
                        type="number"
                        id="headshotKills"
                        name="headshotKills"
                        value={data.headshotKills}
                        onChange={(e) =>
                          setData({ ...data, headshotKills: e.target.value })
                        }
                      />
                    </div>
                    <div className="row">
                      {" "}
                      <label htmlFor="kills">Kills:</label>
                      <input
                        type="number"
                        id="kills"
                        name="kills"
                        value={data.kills}
                        onChange={(e) =>
                          setData({ ...data, kills: e.target.value })
                        }
                      />
                    </div>
                    <div className="row">
                      <label htmlFor="longestKill">Longest Kill:</label>
                      <input
                        type="number"
                        id="longestKill"
                        name="longestKill"
                        value={data.longestKill}
                        onChange={(e) =>
                          setData({ ...data, longestKill: e.target.value })
                        }
                      />
                    </div>
                    <div className="row">
                      <label htmlFor="matchDuration">Match Duration:</label>
                      <input
                        type="number"
                        id="matchDuration"
                        name="matchDuration"
                        value={data.matchDuration}
                        onChange={(e) =>
                          setData({ ...data, matchDuration: e.target.value })
                        }
                      />
                    </div>
                    <div className="row">
                      <label htmlFor="revives">Revives:</label>
                      <input
                        type="number"
                        id="revives"
                        name="revives"
                        value={data.revives}
                        onChange={(e) =>
                          setData({ ...data, revives: e.target.value })
                        }
                      />
                    </div>
                    <div className="row">
                      <label htmlFor="teamKills">Team Kills:</label>
                      <input
                        type="number"
                        id="teamKills"
                        name="teamKills"
                        value={data.teamKills}
                        onChange={(e) =>
                          setData({ ...data, teamKills: e.target.value })
                        }
                      />
                    </div>
                    <div className="row">
                      <label htmlFor="vehicleDestroys">Vehicle Destroys:</label>
                      <input
                        type="number"
                        id="vehicleDestroys"
                        name="vehicleDestroys"
                        value={data.vehicleDestroys}
                        onChange={(e) =>
                          setData({ ...data, vehicleDestroys: e.target.value })
                        }
                      />
                    </div>
                    <div className="row">
                      <label htmlFor="walkDistance">Walk Distance:</label>
                      <input
                        type="number"
                        id="walkDistance"
                        name="walkDistance"
                        value={data.walkDistance}
                        onChange={(e) =>
                          setData({ ...data, walkDistance: e.target.value })
                        }
                      />
                    </div>
                    <div className="row">
                      <label htmlFor="weaponsAcquired">Weapons Acquired:</label>
                      <input
                        type="number"
                        id="weaponsAcquired"
                        name="weaponsAcquired"
                        value={data.weaponsAcquired}
                        onChange={(e) =>
                          setData({ ...data, weaponsAcquired: e.target.value })
                        }
                      />
                    </div>
                    <div className="row">
                      {" "}
                      <label htmlFor="matchType">Match Type:</label>
                      <select
                        id="matchType"
                        name="matchType"
                        value={data.matchType}
                        onChange={(e) =>
                          setData({ ...data, matchType: e.target.value })
                        }
                        required
                      >
                        <option value="">--Select a Match Type--</option>
                        <option value="squad-fpp">Squad FPP</option>
                        <option value="duo-fpp">Duo FPP</option>
                        <option value="squad">Squad</option>
                        <option value="solo-fpp">Solo FPP</option>
                        <option value="duo">Duo</option>
                        <option value="solo">Solo</option>
                        <option value="normal-squad-fpp">
                          Normal Squad FPP
                        </option>
                        <option value="flarefpp">Flare FPP</option>
                        <option value="normal-solo-fpp">Normal Solo FPP</option>
                        <option value="crashfpp">Crash FPP</option>
                        <option value="normal-duo-fpp">Normal Duo FPP</option>
                      </select>
                    </div>

                    <div className="mb-3">
                      <button className="btn btn-primary" type="submit">
                        Predict your pubg Score
                      </button>
                    </div>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
export default TestFormm;
