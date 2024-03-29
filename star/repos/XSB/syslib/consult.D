% THIS FILE IS AUTOMATICALLY GENERATED.
% DO NOT EDIT; ALL CHANGES WILL BE LOST!

:- mode [+|+].
:- mode acceptable_extension(+).
:- mode add_lib_dir(+).
:- mode add_lib_dir(+,+).
:- mode add_lib_dir1(+).
:- mode add_this_lib_dir.
:- mode add_to_in_mod(?,?).
:- mode add_xsb_obj_ext_if_nec(+,?).
:- mode cd_throw(+,?).
:- mode check_dir_exists(+).
:- mode check_one_thread_w_override.
:- mode check_set_mod(?).
:- mode cleanup_for_load.
:- mode close_and_throw(+,+,?).
:- mode compile(+).
:- mode compile(+,+).
:- mode compile0(+,+,+,?).
:- mode compile_f(+,+,+,+,?,+,+).
:- mode compile_load_user(+).
:- mode compile_opt_checked(+,+,+).
:- mode consult(+).
:- mode consult(+,+).
:- mode current_loaded_file(?).
:- mode cvt_back_to_for(+,?).
:- mode cvt_body_to_mod(?,?,?).
:- mode cvt_canonical(+,+).
:- mode cvt_head_to_mod(?,?,?).
:- mode cvt_term_to_mod(?,?).
:- mode cvt_term_to_mod_list(?,+,+,?,?).
:- mode cvt_to_mod(?,?,?,+).
:- mode cvt_to_mod_and_add(?,?,+,?).
:- mode do_assert_and_fail(?,+,+,?,?).
:- mode dotted_ext(+,?).
:- mode engine_mode_magic_num(?,?,?).
:- mode ensure_dyn_loaded(+).
:- mode ensure_dyn_loaded(+,+,+).
:- mode ensure_dyn_loaded_novarcheck(+,+,+).
:- mode ensure_dync_loaded(+).
:- mode ensure_dync_loaded(?,?,?).
:- mode ensure_dync_loaded_novarcheck(?,?,?).
:- mode ensure_loaded(+).
:- mode ensure_loaded(+,+).
:- mode ensure_loaded(+,+,+).
:- mode ensure_loaded_novarcheck(+).
:- mode ensure_loaded_novarcheck(+,+,+).
:- mode execute_accumulated_commands(+).
:- mode file_exists_here_or_configbin_or_configlib(+,?).
:- mode file_is_consultloaded(+).
:- mode file_is_dynloaded(+,?).
:- mode fix_body_goal(?,?,?).
:- mode fix_head_term(?,?,?).
:- mode fmod_from_base(+,?).
:- mode get_HRname(+,+,?,?).
:- mode get_fname(+,?,?,?,?).
:- mode get_magic_num(+,?).
:- mode get_mod_from_filename(+,?).
:- mode has_lib_dir(?).
:- mode i_want_compile(+,+,+).
:- mode if_file_loaded(+).
:- mode if_should_not_reload(+).
:- mode indexes_subsumed(+,+).
:- mode init_for_load(+,+).
:- mode init_in_mod.
:- mode is_loaded(+).
:- mode is_wind(+).
:- mode llappend(?,?,+).
:- mode llappend(+,+,?).
:- mode load_dyn(+).
:- mode load_dyn(+,+).
:- mode load_dyn(+,+,+).
:- mode load_dyn0(+,+,+,+,+,?,?).
:- mode load_dyn1(+,+,+,+,?,?).
:- mode load_dyn_convert(?,?,+).
:- mode load_dyn_gen(?,?).
:- mode load_dyn_nocheck(+,?,?,?).
:- mode load_dyn_read_and_assert(+,+,?,?).
:- mode load_dyna(?).
:- mode load_dync(+).
:- mode load_dync(+,+).
:- mode load_dync(+,+,+).
:- mode load_dync0(+,+,+,+,+,?,?,?).
:- mode load_dync1(+,+,+,+,?,?,?).
:- mode load_dync_nocheck(+,?,?,?,?).
:- mode load_dync_read_and_assert(+,+,+,?,?,?).
:- mode load_dynca(+).
:- mode load_dynca(+,+).
:- mode load_exec(+,+).
:- mode make_filecopy(+,+).
:- mode multifile_cvt(?,?,?).
:- mode multifile_cvt_head(?,?).
:- mode need_more_index(+).
:- mode needs_recompile(+,+,+).
:- mode not_asserted_term(?).
:- mode object_file_magic_mismatch(+).
:- mode pop_loaded_file(?).
:- mode proc_directive(?,?,?).
:- mode proc_dynamic(?,?).
:- mode proc_index(?,?).
:- mode proc_multifile(?).
:- mode proc_table(?,?).
:- mode proc_table_options(?,+).
:- mode push_loaded_file(?,?).
:- mode read_canonical(?).
:- mode read_canonical(+,?).
:- mode real_search_module(+,?,?,?).
:- mode reconsult(+).
:- mode reconsult(+,+).
:- mode reconsult(+,+,+).
:- mode reconsult0(+,+,+).
:- mode record_file_consultloaded(+).
:- mode record_file_dynloaded(+,+).
:- mode remove_file_consultloaded(+).
:- mode remove_file_dynloaded(+).
:- mode remove_lib_dir(+).
:- mode removeall_lib_dir(+).
:- mode se_assert_code_to_buff(?).
:- mode search_module(+,?,?,?,?,?).
:- mode set_module_type(?).
:- mode set_retracted(+,+,+,+,?,?,?).
:- mode split_xsb_filename(+,?,?,?).
:- mode standardize_pathname(?,?).
:- mode thread_private(?).
:- mode thread_shared(?).
:- mode write_canonical_list(?).
:- mode xsb_filename(+,?).

:- mode_on_success [g|g].
:- mode_on_success acceptable_extension(g).
:- mode_on_success add_lib_dir(g).
:- mode_on_success add_lib_dir(g,g).
:- mode_on_success add_lib_dir1(g).
:- mode_on_success add_this_lib_dir.
:- mode_on_success add_to_in_mod(A,B).
:- mode_on_success add_xsb_obj_ext_if_nec(g,g).
:- mode_on_success check_dir_exists(g).
:- mode_on_success check_one_thread_w_override.
:- mode_on_success check_set_mod(A).
:- mode_on_success cleanup_for_load.
:- mode_on_success compile(g).
:- mode_on_success compile(g,g).
:- mode_on_success compile0(g,g,g,A).
:- mode_on_success compile_f(g,g,g,g,A,g,g).
:- mode_on_success compile_load_user(g).
:- mode_on_success compile_opt_checked(g,g,g).
:- mode_on_success consult(g).
:- mode_on_success consult(g,g).
:- mode_on_success current_loaded_file(A).
:- mode_on_success cvt_back_to_for(g,g).
:- mode_on_success cvt_body_to_mod(A,B,A).
:- mode_on_success cvt_body_to_mod(ng,A,B).
:- mode_on_success cvt_canonical(g,g).
:- mode_on_success cvt_head_to_mod(A,B,g).
:- mode_on_success cvt_head_to_mod(ng,A,ng).
:- mode_on_success cvt_term_to_mod(A,g).
:- mode_on_success cvt_term_to_mod(ng,ng).
:- mode_on_success cvt_term_to_mod_list(A,g,g,B,g).
:- mode_on_success cvt_term_to_mod_list(ng,g,g,A,ng).
:- mode_on_success cvt_to_mod(A,B,A,g).
:- mode_on_success cvt_to_mod_and_add(A,B,g,A).
:- mode_on_success dotted_ext(g,g).
:- mode_on_success engine_mode_magic_num(g,g,g).
:- mode_on_success ensure_dyn_loaded(g).
:- mode_on_success ensure_dyn_loaded(g,g,g).
:- mode_on_success ensure_dyn_loaded_novarcheck(g,g,g).
:- mode_on_success ensure_dync_loaded(g).
:- mode_on_success ensure_dync_loaded(g,A,B).
:- mode_on_success ensure_dync_loaded_novarcheck(g,A,B).
:- mode_on_success ensure_loaded(g).
:- mode_on_success ensure_loaded(g,g).
:- mode_on_success ensure_loaded(g,g,g).
:- mode_on_success ensure_loaded_novarcheck(g).
:- mode_on_success ensure_loaded_novarcheck(g,g,g).
:- mode_on_success execute_accumulated_commands(g).
:- mode_on_success file_exists_here_or_configbin_or_configlib(g,g).
:- mode_on_success file_is_consultloaded(g).
:- mode_on_success file_is_dynloaded(g,g).
:- mode_on_success fix_body_goal(A,B,A).
:- mode_on_success fix_body_goal(ng,A,B).
:- mode_on_success fix_head_term(g,A,g).
:- mode_on_success fix_head_term(ng,A,B).
:- mode_on_success fmod_from_base(g,g).
:- mode_on_success get_HRname(g,g,g,g).
:- mode_on_success get_fname(g,g,g,g,g).
:- mode_on_success get_magic_num(g,g).
:- mode_on_success get_mod_from_filename(g,g).
:- mode_on_success has_lib_dir(A).
:- mode_on_success i_want_compile(g,g,g).
:- mode_on_success if_file_loaded(g).
:- mode_on_success if_should_not_reload(g).
:- mode_on_success indexes_subsumed(g,g).
:- mode_on_success init_for_load(g,g).
:- mode_on_success init_in_mod.
:- mode_on_success is_loaded(g).
:- mode_on_success is_wind(g).
:- mode_on_success llappend(g,g,g).
:- mode_on_success load_dyn(g).
:- mode_on_success load_dyn(g,g).
:- mode_on_success load_dyn(g,g,g).
:- mode_on_success load_dyn0(g,g,g,g,g,A,B).
:- mode_on_success load_dyn1(g,g,g,g,A,B).
:- mode_on_success load_dyn_convert(g,g,g).
:- mode_on_success load_dyn_gen(g,g).
:- mode_on_success load_dyn_nocheck(g,g,A,B).
:- mode_on_success load_dyn_option(A,B).
:- mode_on_success load_dyn_read_and_assert(g,g,A,B).
:- mode_on_success load_dyna(g).
:- mode_on_success load_dync(g).
:- mode_on_success load_dync(g,g).
:- mode_on_success load_dync(g,g,g).
:- mode_on_success load_dync0(g,g,g,g,g,A,B,C).
:- mode_on_success load_dync1(g,g,g,g,A,B,C).
:- mode_on_success load_dync_nocheck(g,g,A,B,C).
:- mode_on_success load_dync_read_and_assert(g,g,g,A,B,C).
:- mode_on_success load_dynca(g).
:- mode_on_success load_dynca(g,g).
:- mode_on_success load_exec(g,g).
:- mode_on_success make_filecopy(g,g).
:- mode_on_success multifile_cvt(A,B,C).
:- mode_on_success multifile_cvt_head(A,A).
:- mode_on_success need_more_index(g).
:- mode_on_success needs_recompile(g,g,g).
:- mode_on_success not_asserted_term(A).
:- mode_on_success object_file_magic_mismatch(g).
:- mode_on_success pop_loaded_file(A).
:- mode_on_success proc_directive(g,A,B).
:- mode_on_success proc_dynamic(g,A).
:- mode_on_success proc_index(A,B).
:- mode_on_success proc_multifile(A).
:- mode_on_success proc_table(g,A).
:- mode_on_success proc_table_options(g,g).
:- mode_on_success push_loaded_file(g,g).
:- mode_on_success read_canonical(A).
:- mode_on_success read_canonical(g,A).
:- mode_on_success real_search_module(g,g,g,g).
:- mode_on_success reconsult(g).
:- mode_on_success reconsult(g,g).
:- mode_on_success reconsult(g,g,g).
:- mode_on_success reconsult0(g,g,g).
:- mode_on_success record_file_consultloaded(g).
:- mode_on_success record_file_dynloaded(g,g).
:- mode_on_success remove_file_consultloaded(g).
:- mode_on_success remove_file_dynloaded(g).
:- mode_on_success remove_lib_dir(g).
:- mode_on_success remove_xwam_and_throw(A,B).
:- mode_on_success removeall_lib_dir(g).
:- mode_on_success se_assert_code_to_buff(A).
:- mode_on_success search_module(g,g,g,g,g,g).
:- mode_on_success set_module_type(A).
:- mode_on_success set_retracted(g,g,g,g,g,g,g).
:- mode_on_success split_xsb_filename(g,g,g,g).
:- mode_on_success standardize_pathname(g,g).
:- mode_on_success (thread_private A).
:- mode_on_success (thread_shared A).
:- mode_on_success write_canonical_list(A).
:- mode_on_success xsb_filename(g,g).
