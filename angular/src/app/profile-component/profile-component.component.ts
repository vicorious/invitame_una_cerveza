import { Component, OnInit } from '@angular/core';
import { faHands } from '@fortawesome/free-solid-svg-icons';
import { NgxSpinnerService } from 'ngx-spinner';
import { ToastrService } from 'ngx-toastr';


@Component({
  selector: 'app-profile-component',
  templateUrl: './profile-component.component.html',
  styleUrls: ['./profile-component.component.css']
})
export class ProfileComponentComponent implements OnInit 
{
  
	faHands = faHands;

  constructor(private spinner: NgxSpinnerService, private toast: ToastrService) { }

  ngOnInit() 
  {
    this.spinner.show();
		setTimeout(() => {
			this.spinner.hide();
		  }, 2000);		
  }

}
