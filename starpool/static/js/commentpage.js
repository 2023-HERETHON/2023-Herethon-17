const stars = document.querySelectorAll(".rating__star");
const result = document.querySelector(".rating__result");
const ratingInput = document.getElementById("rating_input");

stars.forEach((star) => {
  star.addEventListener("click", () => {
    const selectedStars = document.querySelectorAll(".rated__star");

    // 선택한 별점 개수 계산
    const ratingCount = selectedStars.length;

    // 선택한 별점 개수를 결과 영역에 표시
    result.textContent = ratingCount;

    // 선택한 별점 개수를 평가 입력 필드에 설정
    ratingInput.value = ratingCount;

    // 선택한 별점 개수에 따라 CSS 클래스 변경
    stars.forEach((star) => {
      if (star.classList.contains("rated__star")) {
        star.classList.remove("far");
        star.classList.add("fas");
      } else {
        star.classList.remove("fas");
        star.classList.add("far");
      }
    });
  });
});
