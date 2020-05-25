import { Component, OnInit } from '@angular/core';
import { faUserTie } from '@fortawesome/free-solid-svg-icons';
import { NgxSpinnerService } from 'ngx-spinner';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-codigo-component',
  templateUrl: './codigo-component.component.html',
  styleUrls: ['./codigo-component.component.css']
})
export class CodigoComponentComponent implements OnInit 
{
  faUserTie = faUserTie;

  constructor(private spinner: NgxSpinnerService, private toast: ToastrService) { }

  ngOnInit() {
    
    this.spinner.show();
		setTimeout(() => {
			this.spinner.hide();
		  }, 2000);		

  }
}
