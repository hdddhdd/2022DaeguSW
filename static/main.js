$(document).ready(function () {
    $('.menu').each(function (index) {
        $(this).attr('menu-index', index);
    }).click(function () {

        // 클릭된 상태면 클릭했을 때 해제 / 안된상태면 선택
        var index = $(this).attr('menu-index');
        console.log(index);

        $('.menu[menu-index=' + index + ']').addClass('clicked_menu');
        $('.menu[menu-index!=' + index + ']').removeClass('clicked_menu');
    });
});


//삭제할 내용