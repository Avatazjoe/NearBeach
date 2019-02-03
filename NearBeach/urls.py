from django.urls import path, include


#The following two imports are for the static files
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path


#Password reset
from django.contrib.auth import views as auth_views


from . import views, \
	views_lookup, \
	views_quotes, \
	views_project_information, \
	views_task_information, \
	views_organisation_information, \
	views_customer_information, \
	views_document_tree, \
	views_requirements, \
	views_administration


urlpatterns = [
re_path(r'^$', views.index, name='index'),
re_path(r'^add_campus_to_customer/(?P<customer_id>[0-9]+)/(?P<campus_id>[0-9]+)/', views.add_campus_to_customer,name='add_campus_to_customer'),
re_path(r'^admin_group/(?P<location_id>[0-9]+)/(?P<destination>["group","permission_set","user"])',views.admin_group,name="admin_group"),
re_path(r'^admin_permission_set/(?P<group_id>[0-9]+)/',views.admin_permission_set,name="admin_permission_set"),
re_path(r'^admin_add_user/(?P<group_id>[0-9]+)/', views.admin_add_user, name="admin_add_user"),
re_path(r'^alerts/',views.alerts,name='alerts'),
re_path(r'^assign_customer_project_task/(?P<customer_id>[0-9]+)/', views.assign_customer_project_task,name='assign_customer_project_task'),
re_path(r'^assigned_group_add/(?P<location_id>[0-9]+)/(?P<destination>["project","task","requirement","quote","kanban_board","opportunity"]+)/$', views.assigned_group_add , name='assigned_group_add'),
re_path(r'^assigned_group_delete/(?P<object_assignment_id>[0-9]+)/', views.assigned_group_delete , name='assigned_group_delete'),
re_path(r'^assigned_group_list/(?P<location_id>[0-9]+)/(?P<destination>["project","task","requirement","quote","kanban_board","opportunity"]+)/', views.assigned_group_list , name='assigned_group_list'),
re_path(r'^assigned_user_add/(?P<location_id>[0-9]+)/(?P<destination>["project","task","requirement","quote","kanban_board","opportunity"]+)/$',views.assigned_user_add,name='assigned_user_add'),
re_path(r'^assigned_user_delete/(?P<object_assignment_id>[0-9]+)/', views.assigned_user_delete , name='assigned_user_delete'),
re_path(r'^assigned_user_list/(?P<location_id>[0-9]+)/(?P<destination>["project","task","requirement","quote","kanban_board","opportunity"]+)/$',views.assigned_user_list,name='assigned_user_list'),
re_path(r'^associate/(?P<project_id>[0-9]+)/(?P<task_id>[0-9]+)/(?P<project_or_task>[P,T])', views.associate,name='associate'),
re_path(r'^associated_projects/(?P<task_id>[0-9]+)/', views.associated_projects, name='associated_projects'),
re_path(r'^associated_task/(?P<project_id>[0-9]+)/', views.associated_task, name='associated_task'),
re_path(r'^bug_add/(?P<location_id>[0-9]+)/(?P<destination>["project","task","requirement"]+)/(?P<bug_id>[0-9]+)/(?P<bug_client_id>[0-9]+)',views.bug_add,name='bug_add'),
re_path(r'^bug_client_delete/(?P<bug_client_id>[0-9]+)/$', views.bug_client_delete, name='bug_client_delete'),
re_path(r'^bug_client_information/(?P<bug_client_id>[0-9]+)/$', views.bug_client_information,name='bug_client_information'),
re_path(r'^bug_client_list/$',views.bug_client_list,name='bug_client_list'),
re_path(r'^bug_list/(?P<location_id>[0-9]+)/(?P<destination>["project","task","requirement"]+)/$', views.bug_list, name='bug_list'),
re_path(r'^bug_list/$', views.bug_list, name='bug_list'),
re_path(r'^bug_search/(?P<location_id>[0-9]+)/(?P<destination>["project","task","requirement"]+)/$', views.bug_search, name='bug_search'),
re_path(r'^campus_information/(?P<campus_information>[0-9]+)/', views.campus_information, name='campus_information'),
re_path(r'^campus_readonly/(?P<campus_information>[0-9]+)/', views.campus_readonly, name='campus_readonly'),
re_path(r'^cost_information/(?P<location_id>[0-9]+)/(?P<destination>["project","task"]+)/$',views.cost_information,name='cost_information'),
re_path(r'^customer_information/(?P<customer_id>[0-9]+)/', views.customer_information, name='customer_information'),
re_path(r'^customer_campus_information/(?P<customer_campus_id>[0-9]+)/(?P<customer_or_org>["CUST","CAMP"]+)',views.customer_campus_information, name="customer_campus_information"),
re_path(r'^customer_readonly/(?P<customer_id>[0-9]+)/', views.customer_readonly, name='customer_readonly'),
re_path(r'^dashboard/$', views.dashboard,name='dashboard'),
re_path(r'^dashboard/active_projects', views.dashboard_active_projects,name='dashboard_active_projects'),
re_path(r'^dashboard/active_quotes', views.dashboard_active_quotes,name='dashboard_active_quotes'),
re_path(r'^dashboard/active_requirement', views.dashboard_active_requirement, name='dashboard_active_requirement'),
re_path(r'^dashboard/active_task', views.dashboard_active_task, name='dashboard_active_task'),
re_path(r'^dashboard/group_active_projects', views.dashboard_group_active_projects,name='dashboard_group_active_projects'),
re_path(r'^dashboard/group_active_task', views.dashboard_group_active_task,name='dashboard_group_active_task'),
re_path(r'^dashboard/group_opportunities', views.dashboard_group_opportunities, name='dashboard_group_opportunities'),
re_path(r'^dashboard/opportunities', views.dashboard_opportunities, name='dashboard_opportunities'),
re_path(r'^deactivate_campus/(?P<campus_id>[0-9]+)/$',views.deactivate_campus,name='deactivate_campus'),
re_path(r'^delete_campus_contact/(?P<customer_campus_id>[0-9]+)/(?P<cust_or_camp>["CUST","CAMP"]+)',views.delete_campus_contact, name='delete_campus_contact'),
re_path(r'^delete_cost/(?P<cost_id>[0-9]+)/(?P<location_id>[0-9]+)/(?P<project_or_task>[P,T])', views.delete_cost,name='delete_cost'),
re_path(r'^delete_document/(?P<document_key>[0-9A-Za-z_\-]+)/$', views_document_tree.delete_document, name='delete_document'),
re_path(r'^delete_folder/(?P<folder_id>[0-9]+)/$', views_document_tree.delete_folder, name='delete_folder'),
re_path(r'^diagnostic_information/$', views.diagnostic_information, name='diagnostic_information'),
re_path(r'^diagnostic_test_database/',views.diagnostic_test_database,name='diagnostic_test_database'),
re_path(r'^diagnostic_test_document_upload/',views.diagnostic_test_document_upload,name='diagnostic_test_document_upload'),
re_path(r'^diagnostic_test_email/',views.diagnostic_test_email,name='diagnostic_test_email'),
re_path(r'^diagnostic_test_location_services/',views.diagnostic_test_location_services,name='diagnostic_test_location_services'),
re_path(r'^diagnostic_test_recaptcha/',views.diagnostic_test_recaptcha,name='diagnostic_test_recaptcha'),
re_path(r'^document_tree_folder/(?P<location_id>[0-9]+)/(?P<destination>["project","task","requirement","quote","kanban_board","opportunity","organisation","customer"]+)/(?P<folder_id>[0-9]+)/$', views_document_tree.document_tree_folder,name='document_tree_folder'),
re_path(r'^document_tree_list/(?P<location_id>[0-9]+)/(?P<destination>["project","task","requirement","quote","kanban_board","opportunity","organisation","customer"]+)/(?P<folder_id>[0-9]+)/', views_document_tree.document_tree_list,name='document_tree_list'),
re_path(r'^document_tree_list/(?P<location_id>[0-9]+)/(?P<destination>["project","task","requirement","quote","kanban_board","opportunity","organisation","customer"]+)/$', views_document_tree.document_tree_list,name='document_tree_list'),
re_path(r'^document_tree_upload/(?P<location_id>[0-9]+)/(?P<destination>["project","task","requirement","quote","kanban_board","opportunity","organisation","customer"]+)/(?P<folder_id>[0-9]+)/$', views_document_tree.document_tree_upload,name="document_tree_upload"),
re_path(r'^document_tree_url/(?P<location_id>[0-9]+)/(?P<destination>["project","task","requirement","quote","kanban_board","opportunity","organisation","customer"]+)/(?P<folder_id>[0-9]+)/$', views_document_tree.document_tree_url,name='document_tree_url'),
re_path(r'^email_history/(?P<location_id>[0-9]+)/(?P<destination>["organisation","customer","project","task","opportunity","quote"]+)/$', views.email_history,name='email_history'),
re_path(r'^email_information/(?P<email_content_id>[0-9]+)/$', views.email_information,name='email_information'),
re_path(r'^email/(?P<location_id>[0-9]+)/(?P<destination>["organisation","customer","project","task","opportunity","quote"]+)/$', views.email,name='email'),
re_path(r'^extract_quote/(?P<quote_uuid>[0-9A-Za-z_\-]+)/(?P<quote_template_id>[0-9]+)/', views.extract_quote,name='extract_quote'),
re_path(r'^group_information/(?P<group_id>[0-9]+)/$',views.group_information,name='group_information'),
re_path(r'^information_customer_contact_history/(?P<customer_id>[0-9]+)/$',views_customer_information.information_customer_contact_history,name='information_customer_contact_history'),
re_path(r'^information_organisation_contact_history/(?P<organisation_id>[0-9]+)/$',views_organisation_information.information_organisation_contact_history,name='information_organisation_contact_history'),
re_path(r'^information_project_customer/(?P<project_id>[0-9]+)/$', views_project_information.information_project_customer, name='information_project_customer'),
re_path(r'^information_project_history/(?P<project_id>[0-9]+)/$', views_project_information.information_project_history, name='information_project_history'),
re_path(r'^information_task_customer/(?P<task_id>[0-9]+)/$', views_task_information.information_task_customer,name='information_task_customer'),
re_path(r'^information_task_history/(?P<task_id>[0-9]+)/$', views_task_information.information_task_history,name='information_task_history'),
re_path(r'^kanban_edit_card/(?P<kanban_card_id>[0-9]+)/$', views.kanban_edit_card,name='kanban_edit_card'),
re_path(r'^kanban_edit_xy_name/(?P<location_id>[0-9]+)/(?P<destination>["column","level"]+)/$', views.kanban_edit_xy_name,name='kanban_edit_xy_name'),
re_path(r'^kanban_information/(?P<kanban_board_id>[0-9]+)/', views.kanban_information, name='kanban_information'),
re_path(r'^kanban_list/', views.kanban_list,name='kanban_list'),
re_path(r'^kanban_move_card/(?P<kanban_card_id>[0-9]+)/(?P<kanban_column_id>[0-9]+)/(?P<kanban_level_id>[0-9]+)/', views.kanban_move_card, name='kanban_move_card'),
re_path(r'^kanban_new_card/(?P<kanban_board_id>[0-9]+)/$', views.kanban_new_card,name='kanban_new_card'),
re_path(r'^kanban_new_link/(?P<kanban_board_id>[0-9]+)/(?P<location_id>[0-9]+)/(?P<destination>["project","task","requirement"]+)/$', views.kanban_new_link,name='kanban_new_link'),
re_path(r'^kanban_new_link/(?P<kanban_board_id>[0-9]+)/$', views.kanban_new_link,name='kanban_new_link'),
re_path(r'^kanban_properties/(?P<kanban_board_id>[0-9]+)/$', views.kanban_properties,name='kanban_properties'),
re_path(r'^kanban_requirement_information/(?P<kanban_board_id>[0-9]+)/$',views.kanban_requirement_information,name='kanban_requirement_information'),
re_path(r'^kanban_requirement_item_update/(?P<requirement_item_id>[0-9]+)/(?P<status_id>[0-9]+)/$',views.kanban_requirement_item_update,name="kanban_requirement_item_update"),
re_path(r'^kudos_rating/(?P<kudos_key>[0-9A-Za-z_\-]+)/$', views.kudos_rating, name='kudos_rating'),
re_path(r'^kudos_read_only/(?P<kudos_key>[0-9A-Za-z_\-]+)/$', views.kudos_read_only, name='kudos_read_only'),
re_path(r'^list_of_taxes_deactivate/(?P<tax_id>[0-9]+)/', views_administration.list_of_taxes_deactivate, name='list_of_taxes_deactivate'),
re_path(r'^list_of_taxes_edit/(?P<tax_id>[0-9]+)/', views_administration.list_of_taxes_edit, name='list_of_taxes_edit'),
re_path(r'^list_of_taxes_information/', views_administration.list_of_taxes_information, name='list_of_taxes_information'),
re_path(r'^list_of_taxes_list/', views_administration.list_of_taxes_list, name='list_of_taxes_list'),
re_path(r'^list_of_taxes_new/', views_administration.list_of_taxes_new, name='list_of_taxes_new'),
re_path(r'^login', views.login, name='login'),
re_path(r'^logout', views.logout, name='logout'),
re_path(r'^lookup_product/(?P<product_id>[0-9]+)/$', views_lookup.lookup_product, name='lookup_product'),
re_path(r'^my_profile', views.my_profile,name='my_profile'),
re_path(r'^new_bug_client/$',views.new_bug_client, name='new_bug_client'),
re_path(r'^new_campus/(?P<location_id>[0-9]+)/(?P<destination>["organisation","customer"]+)/$', views.new_campus, name='new_campus'),
re_path(r'^new_customer/(?P<organisation_id>[0-9]+)/', views.new_customer, name='new_customer'),
re_path(r'^new_group/',views.new_group,name="new_group"),
re_path(r'^new_kanban_board/$', views.new_kanban_board,name='new_kanban_board'),
re_path(r'^new_kanban_requirement_board/(?P<requirement_id>[0-9]+)/',views.new_kanban_requirement_board,name='new_kanban_requirement_board'),
re_path(r'^new_kudos/(?P<project_id>[0-9]+)/',views.new_kudos,name='new_kudos'),
re_path(r'^new_opportunity/(?P<location_id>[0-9]+)/(?P<destination>["customer","organisation"]+)/$', views.new_opportunity,name='new_opportunity'),
re_path(r'^new_opportunity/$', views.new_opportunity, name='new_opportunity'),
re_path(r'^new_organisation', views.new_organisation, name='new_organisation'),
re_path(r'^new_permission_set/', views.new_permission_set, name='new_permission_set'),
re_path(r'^new_project/(?P<location_id>[0-9]+)/(?P<destination>["customer","organisation","opportunity"]+)/$',views.new_project,name='new_project'),
re_path(r'^new_project/$', views.new_project, name='new_project'),
re_path(r'^new_quote_template/',views.new_quote_template,name='new_quote_template'),
re_path(r'^new_quote/(?P<primary_key>[0-9]+)/(?P<destination>["project","task","opportunity","customer","organisation"]+)/',views.new_quote, name='new_quote'),
re_path(r'^new_requirement/', views_requirements.new_requirement,name="new_requirement"),
re_path(r'^new_task/(?P<location_id>[0-9]+)/(?P<destination>["organisation","customer","opportunity"]+)/$', views.new_task, name='new_task'),
re_path(r'^new_task/$', views.new_task, name='new_task'),
re_path(r'^new_user/$', views_administration.new_user, name='new_user'),
re_path(r'^opportunity_information/(?P<opportunity_id>[0-9]+)/', views.opportunity_information,name='opportunity_information'),
re_path(r'^organisation_information/(?P<organisation_id>[0-9]+)/', views.organisation_information,name='organisation_information'),
re_path(r'^organisation_readonly/(?P<organisation_id>[0-9]+)/', views.organisation_readonly,name='organisation_readonly'),
re_path(r'^permission_denied', views.permission_denied, name='permission_denied'),
re_path(r'^permission_set_information/(?P<permission_set_id>[0-9]+)/$',views.permission_set_information,name='permission_set_information'),
re_path(r'^preview_quote/(?P<quote_uuid>[0-9A-Za-z_\-]+)/(?P<quote_template_id>[0-9]+)/',views.preview_quote,name='preview_quote'),
re_path(r'^private/(?P<document_key>[0-9A-Za-z_\-]+)/$', views.private_document, name='private'),
re_path(r'^product_and_service_discontinued/(?P<product_id>[0-9]+)/', views_administration.product_and_service_discontinued, name='product_and_service_discontinued'),
re_path(r'^product_and_service_edit/(?P<product_id>[0-9]+)/', views_administration.product_and_service_edit, name='product_and_service_edit'),
re_path(r'^product_and_service_new/', views_administration.product_and_service_new, name='product_and_service_new'),
re_path(r'^product_and_service_search/', views_administration.product_and_service_search, name='product_and_service_search'),
re_path(r'^project_information/(?P<project_id>[0-9]+)/', views.project_information, name='project_information'),
re_path(r'^project_readonly/(?P<project_id>[0-9]+)/', views.project_readonly, name='project_readonly'),
re_path(r'^project_remove_customer/(?P<project_customer_id>[0-9]+)/',views.project_remove_customer,name='project_remove_customer'),
re_path(r'^quote_delete_line_item/(?P<line_item_id>[0-9]+)/$', views_quotes.delete_line_item, name='quote_delete_line_item'),
re_path(r'^quote_delete_responsible_customer/(?P<quote_id>[0-9]+)/(?P<customer_id>[0-9]+)/$', views_quotes.delete_responsible_customer, name='quote_delete_responsible_customer'),
re_path(r'^quote_information/(?P<quote_id>[0-9]+)/$', views.quote_information, name='quote_information'),
re_path(r'^quote_list_of_line_items/(?P<quote_id>[0-9]+)/$', views_quotes.list_of_line_items, name='quote_list_of_line_items'),
re_path(r'^quote_new_line_item/(?P<quote_id>[0-9]+)/$', views_quotes.new_line_item, name='quote_new_line_item'),
re_path(r'^quote_readonly/(?P<quote_id>[0-9]+)/$', views.quote_readonly, name='quote_readonly'),
re_path(r'^quote_responsible_customer/(?P<quote_id>[0-9]+)/(?P<customer_id>[0-9]+)/$', views_quotes.responsible_customer, name='quote_responsible_customer'),
re_path(r'^quote_responsible_customer/(?P<quote_id>[0-9]+)/$', views_quotes.responsible_customer, name='quote_responsible_customer'),
re_path(r'^quote_template_information/(?P<quote_template_id>[0-9]+)/',views.quote_template_information,name='quote_template_information'),
re_path(r'^rename_document/(?P<document_key>[0-9A-Za-z_\-]+)/$', views.rename_document, name='rename_document'),
re_path(r'^requirement_documents_uploads/(?P<location_id>[0-9]+)/(?P<destination>["requirement","requirement_item"]+)', views_requirements.requirement_documents_uploads, name='requirement_documents_uploads'),
re_path(r'^requirement_information/(?P<requirement_id>[0-9]+)/', views_requirements.requirement_information,name="requirement_information"),
re_path(r'^requirement_item_edit/(?P<requirement_item_id>[0-9]+)/', views_requirements.requirement_item_edit,name="requirement_item_edit"),
re_path(r'^requirement_items_list/(?P<requirement_id>[0-9]+)/', views_requirements.requirement_items_list,name="requirement_items_list"),
re_path(r'^requirement_items_new_link/(?P<requirement_item_id>[0-9]+)/(?P<location_id>[0-9]+)/(?P<destination>["project","task","organisation"]+)',views_requirements.requirement_items_new_link, name="requirement_items_new_link"),
re_path(r'^requirement_items_new_link/(?P<requirement_item_id>[0-9]+)/$', views_requirements.requirement_items_new_link,name="requirement_items_new_link"),
re_path(r'^requirement_items_new/(?P<requirement_id>[0-9]+)/', views_requirements.requirement_items_new,name="requirement_items_new"),
re_path(r'^requirement_links_list/(?P<requirement_id>[0-9]+)/', views_requirements.requirement_links_list,name="requirement_links_list"),
re_path(r'^requirement_new_link/(?P<requirement_id>[0-9]+)/(?P<location_id>[0-9]+)/(?P<destination>["project","task","organisation"]+)', views_requirements.requirement_new_link,name="requirement_new_link"),
re_path(r'^requirement_new_link/(?P<requirement_id>[0-9]+)/$', views_requirements.requirement_new_link,name="requirement_new_link"),
re_path(r'^requirement_readonly/(?P<requirement_id>[0-9]+)/$', views_requirements.requirement_readonly,name="requirement_readonly"),
re_path(r'^resolve_project/(?P<project_id>[0-9]+)/', views.resolve_project,    name='resolve_project'),
re_path(r'^resolve_task/(?P<task_id>[0-9]+)/', views.resolve_task, name='resolve_task'),
re_path(r'^search_customer', views.search_customer, name='search_customer'),
re_path(r'^search_group', views.search_group, name='search_group'),
re_path(r'^search_organisation', views.search_organisation, name='search_organisation'),
re_path(r'^search_permission_set', views.search_permission_set, name='search_permission_set'),
re_path(r'^search_projects_task', views.search_projects_task, name='search_projects_task'),
re_path(r'^search_templates/',views.search_templates,name='search_templates'),
re_path(r'^search_users', views_administration.search_users, name='search_users'),
re_path(r'^search/', views.search, name='search'),
re_path(r'^task_information/(?P<task_id>[0-9]+)', views.task_information, name='task_information'),
re_path(r'^task_readonly/(?P<task_id>[0-9]+)', views.task_readonly, name='task_readonly'),
re_path(r'^task_remove_customer/(?P<task_customer_id>[0-9]+)/',views.task_remove_customer,name='task_remove_customer'),
re_path(r'^timeline_data/$', views.timeline_data, name='timeline_data'),
re_path(r'^timeline/$', views.timeline, name='timeline'),
re_path(r'^to_do_complete/(?P<to_do_id>[0-9]+)/$', views.to_do_complete, name='to_do_complete'),
re_path(r'^to_do/(?P<location_id>[0-9]+)/(?P<destination>["project","task","opportunity"]+)/$', views.to_do_list, name='to_do'),
re_path(r'^user_information/(?P<user_id>[0-9]+)/$', views_administration.user_information, name='user_information'),
re_path(r'^user_permissions', views_lookup.lookup_user_permissions, name='user_permissions'),
re_path(r'^user_want_remove/(?P<user_want_id>[0-9]+)', views.user_want_remove,name="user_want_remove"),
re_path(r'^user_want_view', views.user_want_view,name='user_want_view'),
re_path(r'^user_weblink_remove/(?P<user_weblink_id>[0-9]+)',views.user_weblink_remove,name='user_weblink_remove'),
re_path(r'^user_weblink_view',views.user_weblink_view,name='user_weblink_view'),

	path('change-password/', auth_views.PasswordChangeView.as_view()),
	path(
		'password_reset/',
		auth_views.PasswordResetView.as_view(
			template_name='NearBeach/password_reset.html',
		),
		name='password_reset',
	),
	path(
		'password_reset/done/',
		auth_views.PasswordResetDoneView.as_view(
			template_name='NearBeach/password_reset_done.html',
		),
		name='password_reset_done',
	),
	path(
		'reset/<uidb64>/<token>/',
		auth_views.PasswordResetConfirmView.as_view(
			template_name='NearBeach/reset.html',
		),
		name='password_reset_confirm',
	),
	path(
		'reset/done',
		auth_views.PasswordResetCompleteView.as_view(
			template_name='NearBeach/reset_done.html',
		),
		name='password_reset_complete'
	),



]


if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

