import { HttpErrorResponse } from "@angular/common/http";
import { throwError } from "rxjs";

export class CatchError {
    /**
	 * 
	 * @param error 
	 * 
	 */
	public static handleError(error: HttpErrorResponse) 
	{
        return throwError(
        {
            error: error.name,
            message: error.message,
            status: error.status,
            headers: error.headers
        })
    }	
}
