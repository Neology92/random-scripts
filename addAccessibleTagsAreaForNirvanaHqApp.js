// 📘 Simple script modifying NirvanaHq (todo list app) sidebar
// Adds tag filtering button for easier access to current sprint tasks

// 💡 Fired with Page Manipulator extension for Google Chrome:
// https://chrome.google.com/webstore/detail/page-manipulator/mdhellggnoabbnnchkeniomkpghbekko

function insertAfter(newNode, existingNode) {
  existingNode.parentNode.insertBefore(newNode, existingNode.nextSibling);
}

const addCurrentTagButton = () => {
  const tagsCloudcopy = document.querySelector(".tagcloud").cloneNode(true);

  const childrenToRemove = [];
  tagsCloudcopy.firstChild.childNodes.forEach((item) => {
    if (item.getAttribute("rel") !== "gCurrent Sprint")
      childrenToRemove.push(item);
  });

  childrenToRemove.forEach((item) => {
    tagsCloudcopy.firstChild.removeChild(item);
  });

  const focusNode = document.querySelector(".focus");

  insertAfter(tagsCloudcopy, focusNode);
};

setTimeout(addCurrentTagButton, 500);
