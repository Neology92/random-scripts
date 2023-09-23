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

  const inbox = document.querySelector(".inbox").parentElement;

  insertAfter(tagsCloudcopy, inbox);
};

setTimeout(addCurrentTagButton, 1000);
