
// open  https://old.reddit.com/user/ethfinance/submitted/ in browser
// right-clight > inspect > console tab
// submit the below script and it'll output the contents in _data/dailies-historical.yml format

// example: 
// - date: 2024-12-31
//   title: Daily General Discussion - December 31, 2024
//   link: https://reddit.com/r/ethfinance/comments/1hq8bu0/daily_general_discussion_december_31_2024/
//   comments: 445



let dootsOutputString = "";
document.querySelectorAll('.thing .entry').forEach(entry => {
  let title = entry.querySelector('a.title').innerText;
  if (title.includes("Daily General Discussion")){
    let link = entry.querySelector('a.title').getAttribute('href');
    let date = entry.querySelector('.tagline time').getAttribute('datetime').split('T')[0];
    let comments = entry.querySelector('.flat-list .first a.comments').innerText.split(' ')[0];

    let output = `- date: ${date}\n  title: ${title}\n  link: https://reddit.com${link}\n  comments: ${comments}\n`;
    dootsOutputString += output;
  }
})
console.log(dootsOutputString);



