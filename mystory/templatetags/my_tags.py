from django import template
register = template.Library()


@register.filter
def verbose_name(instance):
        return instance


@register.filter
def verbose_name_plural(obj):
    return obj.verbose_name_plural

@register.filter
def get_icon(obj):
	ICON = {
		"Group":"users",
		"User":"user",
		"Image":"picture-o",
		"About":"user-secret",
		"Wedding_Invitation":"heartbeat",
		"Gallery":"camera-retro",
		"Story":"pencil-square-o",
		"Blessing":"gift",
		"Invitee":"male",
		"Menu":"bars",
		"Music":"music",
	} 
	# return ICON.get(obj.object_name)
	return ICON.get(obj.get('object_name'))