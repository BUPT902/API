/**
 * Created by lenovo on 2016/5/6.
 */
/*!
 * jQuery Form Local Storage Plugin v0.1
 * https://github.com/since1986/jquery.formLocalStorage
 *
 * Copyright since1986
 * Released under the MIT license
 */
(function($) {
    $.fn.formLocalStorage = function(options) {

        var form_selector = this.selector;
        var input_selector = form_selector + " :text, "
            + form_selector + " :checkbox, "
            + form_selector + " :radio, "
            + form_selector + " select, "
            + form_selector + " textarea, "
            + form_selector + " [type='date'] "
            + form_selector + " [type='month'] "
            + form_selector + " [type='week'] "
            + form_selector + " [type='time'] "
            + form_selector + " [type='datetime'] "
            + form_selector + " [type='datetime-local'] "
            + form_selector + " [type='url'] "
            + form_selector + " [type='number'] "
            + form_selector + " [type='range'] "
            + form_selector + " [type='search'] "
            + form_selector + " [type='color'] "
            + form_selector + " [type='email']";


        if(options.debug){ console.debug(this); }

        //���ѡ��
        var options = $.extend({
                storage_name_perfix : ( this.context.URL + form_selector + "@" ), //�ݴ������ǰ׺
                storage_events : ['change'], //�����ݴ���¼�
                storage_dom_class : "_jquery_form_local_storage", //�ݴ����ݵ�class(��������ԭʼ�������ݴ�����)
                storage_manual_remove_trigger_selector : "#storage_manual_remove_trigger", //�ֶ�����ݴ�Ĵ�����
                storage_remove_on_submit : true, //�Ƿ��ڱ��ύʱ����ݴ�
                storage_automatic_remove_flag_selector : "input[name='storage_automatic_remove_flag']", //���ڴ����ݴ��Զ���յ�flag��storage_remove_on_submit = false ������²���Ч��
                storage_automatic_remove_flag_value : 1, //���ڴ����ݴ��Զ���յ�flag��value��storage_remove_on_submit = false ������²���Ч��
                load_ready_callback : function(){}, //�ݴ����ݼ�����ϻص�
                save_ready_callback : function(){}, //�ݴ����ݱ�����ϻص�
                remove_ready_callback : function(){}, //�ݴ�����ɾ����ϻص�
                debug : false, //����ģʽ
            },
            options || {});

        if(options.debug){
            $.each(options, function(k, v){
                console.debug(k + ": " + v);
            });
        }

        this.ready(function(){
            storage_load(); //��������Ϻ��localStorage�������ݴ�ı�����
            storage_save(); //��ر����ݱ仯������localStorage FIXME ��̬д������ݼ�ز���
        });

        this.ready(function(){
            if( !options.storage_remove_on_submit && options.storage_automatic_remove_flag_selector != undefined ){ //���ָ�������ڴ����ݴ��Զ���յ�flag
                if( $(options.storage_automatic_remove_flag_selector).val() == options.storage_automatic_remove_flag_value ){ //��flagֵ������������մ˱������ݴ�����
                    storage_remove();
                }
            }
        });

        //���ύʱ����Ϊ
        this.submit(function(){
            if(options.storage_remove_on_submit){ //��ʹ��Ĭ�����õ�storage_remove_on_submit������ύʱ�Զ���մ˱������ݴ�����
                storage_remove();
            }
        });

        //�ֶ���մ˱����ݴ�����
        if(options.storage_manual_remove_trigger_selector != undefined && options.storage_manual_remove_trigger_selector != null){
            $(options.storage_manual_remove_trigger_selector).click(function(){
                storage_remove();
                location.reload(); //ˢ��ҳ��
            });
        }

        function storage_load(){

            var storage_count = 0;
            $(input_selector).each(function(){
                var storage_key = options.storage_name_perfix + this.name;
                var storage_value = localStorage.getItem(storage_key);
                if(storage_value != undefined && storage_value != null){
                    $(this).val(storage_value);
                    $(this).addClass(options.storage_dom_class); //Ϊ�ݴ����ݼ�����ʽ
                    if(options.debug){ console.debug("Load from localStorage [" + storage_key + " : " + storage_value + "]"); };
                    storage_count++;
                }
            });
            if(storage_count > 0) { options.load_ready_callback(); }
        }

        function storage_save(){

            var _events = options.storage_events.join(" ");
            $(input_selector).live(_events, function(){
                if(this.value != undefined && this.value != null){
                    var storage_key = options.storage_name_perfix + this.name;
                    var storage_value = this.value;
                    localStorage.setItem(storage_key, storage_value);
                    $(this).addClass(options.storage_dom_class);
                    if(options.debug){ console.debug("Save to localStorage [" + storage_key + " : " + storage_value + "]"); };
                }
                options.save_ready_callback();
            });
        }

        function storage_remove(){
            $(input_selector).each(function(){
                var storage_key = options.storage_name_perfix + this.name;
                localStorage.removeItem(storage_key);
                $(this).removeClass(options.storage_dom_class); //ȥ���ݴ����ʽ
                if(options.debug){ console.debug("Remove from localStorage [" + storage_key + "]"); };
            });
            options.remove_ready_callback();
        }

        return this;
    };
})(jQuery);