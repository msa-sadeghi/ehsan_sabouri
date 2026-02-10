$(function() {
            // فرزندان مستقیم - فقط p هایی که مستقیماً داخل .container هستند
            $('#directChild').click(function() {
                $('.container > p').css('background-color', 'yellow');
            });
            
            // تمام فرزندان - تمام p ها در هر عمقی
            $('#allDesc').click(function() {
                $('.container p').css('border', '2px solid red');
            });
            
            // عنصر مجاور - فقط اولین p بعد از h2
            $('#adjacent').click(function() {
                $('h2 + p').css('color', 'blue');
            });
            
            // تمام همسطح‌های بعدی
            $('#siblings').click(function() {
                $('h2 ~ p').css('font-weight', 'bold');
            });
        });