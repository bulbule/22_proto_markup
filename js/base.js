var regionList = [" Алтайский край "," Томская область ", " Красноярский край "];
$.each(regionList, function(regionInd) {
     $('div.dropdown-menu.js-regions').append('<a class="dropdown-item" href="#">' + regionList[regionInd] + '</a>');
});
