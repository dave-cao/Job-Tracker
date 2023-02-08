const changeStatus = (event) => {
  let progression_index = 0;
  const progressions = [
    "Applied and Waiting",
    "Interview Process",
    "Offer",
    "Rejected",
  ];

  // grab status
  let status = event.target.querySelector(".status");
  if (!status) {
    // If click on text, still be able to grab status
    status = event.target.parentElement.querySelector(".status");

    if (!status) {
      // if click and still null, grab status double up
      status =
        event.target.parentElement.parentElement.querySelector(".status");
    }
  }

  // Increase status by one
  let counter = 0;
  for (i = 0; i < progressions.length; i += 1) {
    // If we reached the end of status break loop and restart
    if (status.innerHTML == progressions[progressions.length - 1]) {
      counter = progressions.length;
      break;
    }

    // Increase status by one based on current status
    if (status.innerHTML === progressions[i]) {
      status.innerHTML = progressions[i + 1];
      break;
    }
    counter += 1;
  }

  // If we looped through the progressions and no status was found
  if (counter === progressions.length) {
    status.innerHTML = progressions[0];
  }
};
