from django import template
from courses.models import Course

register = template.Library()

@register.simple_tag
def newest_course():
    ''' Gets the most recent cpurse that was added to the library. '''
    return Course.objects.latest('created_at')

@register.inclusion_tag('courses/course_nav.html')
def nav_courses_list():
    '''Returns dictionary of courses to display as navigation pane'''
    courses = Course.objects.all()
    return {'courses': courses}
#We are including a template inside a template unlike including strings on a template. So registering this tag has a different way

@register.filter('time_estimate')
def time_estimate(word_count):
    '''Estimates the number of minutes it will take to complete a step based on the passed-in wordcontent'''
    minutes = round(word_count/20)
    return minutes