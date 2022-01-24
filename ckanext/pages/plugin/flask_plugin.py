# -*- coding: utf-8 -*-

import ckan.plugins as p
import ckan.plugins.toolkit as toolkit

from ckanext.pages.blueprint import pages as pages_blueprint
import ckanext.pages.cli as cli

def get_recent_blog_posts(number = 5, exclude = None):
    blog_list = toolkit.get_action('ckanext_pages_list')(
        None, {'order_publish_date': True, 'private': False, 'page_type': 'blog'}
    )
    new_list = []
    for blog in blog_list:
        if exclude and blog['name'] == exclude:
            continue
        new_list.append(blog)
        if len(new_list) == number:
            break

    return new_list


class MixinPlugin(p.SingletonPlugin):

    p.implements(p.IBlueprint)
    p.implements(p.IClick)
    p.implements(p.ITemplateHelpers)

    def get_blueprint(self):
        return [pages_blueprint]

    def get_commands(self):
        return cli.get_commands()

    def get_helpers(self):
        return {
            'get_recent_blog_posts': get_recent_blog_posts
        }