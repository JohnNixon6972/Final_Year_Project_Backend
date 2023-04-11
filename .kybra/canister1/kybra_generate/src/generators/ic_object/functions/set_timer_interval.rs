use quote::quote;

pub fn generate_set_timer_interval() -> proc_macro2::TokenStream {
    quote! {
        #[pymethod]
        fn _kybra_set_timer_interval(
            &self,
            interval_py_object_ref: PyObjectRef,
            func_py_object_ref: PyObjectRef,
            vm: &VirtualMachine
        ) -> PyObjectRef {
            let interval_as_u64: u64 = interval_py_object_ref.try_from_vm_value(vm).unwrap();
            let interval = core::time::Duration::new(interval_as_u64, 0);

            let closure = move || {
                unsafe {
                    let _kybra_interpreter = _KYBRA_INTERPRETER_OPTION.as_mut().unwrap();
                    let _kybra_scope = _KYBRA_SCOPE_OPTION.as_mut().unwrap();
                    let vm = &_kybra_interpreter.vm;

                    _kybra_unwrap_rust_python_result(vm.invoke(&func_py_object_ref, ()), vm);
                }
            };

            ic_cdk::timer::set_timer_interval(interval, closure).try_into_vm_value(vm).unwrap()
        }
    }
}
