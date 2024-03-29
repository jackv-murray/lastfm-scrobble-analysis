{#
    This macro splits the tags 
    and takes the first one as the main tag
#}

{% macro get_first_tag(tag) -%}

SPLIT(tag, ',')[OFFSET(0)] AS tag

{%- endmacro %}

