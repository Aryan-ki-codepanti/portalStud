const colors = [
    {
        color: "#6200EE",
        shadowColor: "rgba(98, 0, 238, 0.44)"
    },
    {
        color: "#000",
        shadowColor: "rgba(0 , 0, 0 , 0.44)"
    },
    {
        color: "#018786",
        shadowColor: "rgba(1, 135, 135, 0.44)"
    },
    {
        color: "#FC6E51",
        shadowColor: "rgb(252, 110, 81 , 0.44)"
    },
    {
        color: "#3700B3",
        shadowColor: "rgb(55, 0, 179, 0.44)"
    },
    {
        color: "#ADD468",
        shadowColor: "rgb(173, 212, 104 , 0.44)"
    },
    {
        color: "#D8334A",
        shadowColor: "rgb(216, 51, 74 , 0.44)"
    }
];

const getColorSet = count => colors[count % colors.length];

const markSheetContainer = document.querySelector(".marksheet-container");
const marksheets = Array.from(
    markSheetContainer.getElementsByClassName("marksheet")
);

for (let num = 0; num < marksheets.length; num++) {
    const marksheet = marksheets[num];
    const { color, shadowColor } = getColorSet(num);
    marksheet.style.backgroundColor = color;
    marksheet.style.boxShadow = `${shadowColor}  8px 8px 10px`;
}
