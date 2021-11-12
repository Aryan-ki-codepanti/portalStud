const colors = [
    "#6200EE" ,
    "#000" ,
    "#018786" ,
    "#FC6E51" ,
    "#3700B3" ,
    "#ADD468" ,
    "#D8334A"
];

const getColor = count => colors[ (count % colors.length)] ;

const markSheetContainer = document.querySelector(".marksheet-container");
const marksheets = Array.from(markSheetContainer.getElementsByClassName("marksheet"));

for (let num = 0; num < marksheets.length; num++) {
    const marksheet = marksheets[num];
    marksheet.style.backgroundColor = getColor(num);
}
