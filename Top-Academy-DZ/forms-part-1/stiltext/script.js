const textInput = document.getElementById("texteria");
const fontWeightBold = document.getElementById("font_weight_bold");
const textDecorationUnderline = document.getElementById("text_decoration_underline");
const fontStyleItalics = document.getElementById("font_style_italics");
const textAlignRight = document.getElementById("text_align_right");
const textAlignLeft = document.getElementById("text_align_left");
const textAlignJustify = document.getElementById("text_align_justify");

const BTN = document.getElementById("btn");

BTN.addEventListener("click", () => {
    const styledText = document.getElementById("styled_text");
    if (styledText.textContent = textInput.value) {
        styledText.style.display = 'block';
    }
    if (fontWeightBold.checked) {
        styledText.style.fontWeight = 'bold';
    } else {
        styledText.style.fontWeight = '';
    }
    if (textDecorationUnderline.checked) {
        styledText.style.textDecoration = 'underline';
    } else {
        styledText.style.textDecoration = '';
    }
    if (fontStyleItalics.checked) {
        styledText.style.fontStyle = 'italic';
    } else {
        styledText.style.fontStyle = '';
    }
    if (textAlignRight.checked) {
        styledText.style.textAlign = 'right';
    } else if (textAlignLeft.checked) {
        styledText.style.textAlign = 'left';
    } if (textAlignJustify.checked) {
        styledText.style.textAlign = 'justify';
    }
})