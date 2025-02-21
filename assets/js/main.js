---
---


window.onload = load();

function load() {
  // if params detected, open modal
  let params = getQueryParameters();
  if ("id" in params) {
    showModal(params.id)
  }
  updateLinkTargets();
  enableTooltips();
}




// update the url parameters (does not trigger page refresh)
function setQueryParameters(params=false) {
  // pass params as string; "x=i&y=j&z=k"
  params = params ? params : "";
  if (params != "") {
    params = "?" + params;
  }
  let url = window.location.href.split("?")[0] + params;
  window.history.replaceState(null, "", url);
}
// gets the url parameters
function getQueryParameters() {
  try {
    let queryString = location.search.slice(1), params = {};
    queryString.replace(/([^=]*)=([^&]*)&*/g, (_, key, value) => {
      params[key] = value;
    });
    return params;
  } catch {
    return null;
  }
}
// add event listeners to update url params on modal open/close
document.querySelectorAll('.modal').forEach(function(element) {
  element.addEventListener('show.bs.modal', function (event) {
    let params = "id=" + element.id;
    setQueryParameters(params);
  })
  element.addEventListener('hidden.bs.modal', function (event) {
    setQueryParameters();
  })
})
// shows details modal
function showModal(id) {
  try {
    let detailModal = new bootstrap.Modal(document.getElementById(id), {});
    detailModal.show();
  }
  catch {
    console.log(`modal id does not exist: ${id}`);
  }
}




// enable tooltips
function enableTooltips() {
  let tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
  let tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
  })
}


// open external links and pdfs in new tab
function updateLinkTargets() {
  {%- assign site_url = site.url | split: "//" | last -%}
  document.querySelectorAll("a").forEach(link => {
    let href = link.href;
    // set all links to open in new tab
    if (/^(https?:)?\/\//.test(link.href)) {
      link.target = "_blank";
    }
    // if current domain, use same tab
    if (href != undefined && href.includes("{{site_url}}")) {
      link.target = "_self";
    }
    // if relative links, use new tab
    if (href != undefined && !href.includes("https")) {
      link.target = "_self";
    }
    // open all .pdf, .png, .jpg, .mp4 in new tab
    if (/(\.pdf$|\.png$|\.jpe*g$|\.mp4)/.test(href)) {
      link.target = "_blank";
    }
    // if new-tab class, use new tab
    if (link.classList.contains("new-tab")) {
      link.target = "_blank";
    }
  })
}




