function startRace() {
  let interval = setInterval(() => {
    fetch("/race")
      .then(res => res.json())
      .then(data => {
        data.cars.forEach((car, index) => {
          document.getElementById(`car${index + 1}`).style.left = car.position + "%";
        });

        if (data.winner) {
          clearInterval(interval);
          document.getElementById("winner").innerText = `🏆 ${data.winner} wins the race!`;
        }
      });
  }, 700);
}
