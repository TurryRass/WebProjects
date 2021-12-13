from django import template

register = template.Library()

# in the following decorator we are actually just giving a name to what we want to call the below function with and the name here is get_val even though the name could have been something like 'bhal_bhal'.

# in below with @register I am just registering the filter that's it.

# @register.filter(name='bhal_bhal') This could have been also used.
@register.filter(name='get_val')
def get_val(dict,key):
    # The reason we don't use the below is just because the following one will return 'keyError' but the one after that will only return None and we know that none for loop in none will no be iterated and the good thing is that it also does not gives errors atleast when it is used in django template.
    # return dict[key]
    return dict.get(key)