var map = document.querySelector('#map')
var paths = map.querySelectorAll('.map__image a')
var links = map.querySelectorAll('.map__list a')


if(NodeList.prototype.forEach === undefined)
{
	NodeList.prototype.forEach = function(callback) {
		[].forEach.call(this,callback)
	};
}

var activeArea = function(id)
{
		map.querySelectorAll('.is-active').forEach(function (item)
		{
			item.classList.remove('is-active')
		})
		document.querySelector('#list-' + id).classList.add('is-active')
		document.querySelector('#state-' + id).classList.add('is-active')
}

paths.forEach(function (path){
	path.addEventListener('mouseenter', function()
	{
		var id = this.id.replace('state-','')

		activeArea(id)
	})
})

links.forEach(function (link)
{
	link.addEventListener('mouseenter', function()
	{
		var id = this.id.replace('list-','')

		activeArea(id)
	})
})
