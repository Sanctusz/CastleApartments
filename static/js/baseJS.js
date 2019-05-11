function orderIconClicked(idOfIcon, idOfOtherIcon, doc) {
	orderIconColorChanger(idOfIcon, idOfOtherIcon, doc)

}

function orderIconColorChanger(idOfIcon, idOfOtherIcon, doc) {
	doc.getElementById(idOfIcon).style.color = "#F89D13";
	doc.getElementById(idOfOtherIcon).style.color = "#ede6de"; /*or maybe #ffe3c1*/
	console.log("Hér er ég! inni í baseJS.js")
}