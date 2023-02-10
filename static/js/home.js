// const changeStatus = (event) => {
//   let progression_index = 0;
//   const progressions = [
//     "Applied and Waiting",
//     "Interview Process",
//     "Offer",
//     "Rejected",
//   ];
//
//   // grab status
//   let status = event.target.querySelector(".status");
//   if (!status) {
//     // If click on text, still be able to grab status
//     status = event.target.parentElement.querySelector(".status");
//   }
//
//   // Increase status by one
//   let counter = 0;
//   for (i = 0; i < progressions.length; i += 1) {
//     // If we reached the end of status break loop and restart
//     if (status.innerHTML == progressions[progressions.length - 1]) {
//       counter = progressions.length;
//       break;
//     }
//
//     // Increase status by one based on current status
//     if (status.innerHTML === progressions[i]) {
//       status.innerHTML = progressions[i + 1];
//       break;
//     }
//     counter += 1;
//   }
//
//   // If we looped through the progressions and no status was found
//   if (counter === progressions.length) {
//     status.innerHTML = progressions[0];
//   }
//
//   // If we click, change colour
//   // Change colours of list items based on status
//   let listItem = event.target.parentElement;
//   const jobTitle = document.querySelector(".mb-1");
//   const listGroup = document.querySelector(".list-group");
//
//   // If we click on the job title, grab list item
//   // if (listItem === jobTitle) {
//   //   listItem = event.target.parentElement.parentElement.parentElement;
//   //   console.log("here!");
//
//   //   // If we click actual list item,
//   // }
//   //
//
//   console.log(listItem == jobTitle);
//
//   if (listItem === listGroup) {
//     listItem = event.target;
//     console.log("other");
//   }
//
//   console.log(listItem);
//
//   switch (status.innerHTML) {
//     case "Applied and Waiting":
//       console.log("applied and waiting");
//       listItem.style.backgroundColor = "yellow";
//       break;
//     case "Interview Process":
//       console.log("interview process");
//       listItem.style.backgroundColor = "orange";
//       break;
//
//     case "Offer":
//       console.log("offer");
//       listItem.style.backgroundColor = "green";
//       break;
//
//     case "Rejected":
//       console.log("rejected");
//       listItem.style.backgroundColor = "red";
//       break;
//
//     default:
//       console.log("default");
//       listItem.style.backgroundColor = "white";
//   }
// };

// Scroll into original position if page refreshes
document.addEventListener("DOMContentLoaded", function (event) {
  var scrollpos = localStorage.getItem("scrollpos");
  if (scrollpos) window.scrollTo(0, scrollpos);
});

window.onbeforeunload = function (e) {
  localStorage.setItem("scrollpos", window.scrollY);
};
