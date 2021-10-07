// 브라우저 내 모든 요소가 load 되면 실행
window.onload = function () {
  const hamBtn = document.getElementById("hamBtn");
  // 햄버거 메뉴를 가져옴

  function menuVisible() {
    // 실행 시 메뉴의 left 속성을 변경
    const menu = document.getElementById("menu");
    if (menu.style.left === "-300px") {
      // 메뉴가 안보이는 상태
      menu.style.left = 0;
    } else {
      // 메뉴가 보이는 상태
      menu.style.left = "-300px";
    }
  }

  hamBtn.addEventListener("click", menuVisible);
  // click이라는 event가 발생했을 때, 넘겨준 함수를 실행
};
