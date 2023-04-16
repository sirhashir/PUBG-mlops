const statsForm = document.querySelector('#stats-form');
const statsResult = document.querySelector('#stats-result');

statsForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const formData = new FormData(statsForm);

  fetch('/backend', {
    method: 'POST',
    body: formData
  })
  .then(response => response.json())
  .then(data => {
    statsResult.innerHTML = `Assists: ${data.assists}<br>
                              Boosts: ${data.boosts}<br>
                              Headshot Kills: ${data.headshotKills}<br>
                              Kills: ${data.kills}<br>
                              Longest Kill: ${data.longestKill}<br>
                              Match Duration: ${data.matchDuration}<br>
                              Revives: ${data.revives}<br>
                              Team Kills: ${data.teamKills}<br>
                              Vehicle Destroys: ${data.vehicleDestroys}<br>
                              Walk Distance: ${data.walkDistance}<br>
                              Weapons Acquired: ${data.weaponsAcquired}`;
  })
  .catch(error => console.error(error));
});
