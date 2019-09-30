import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CuriosoComponentComponent } from './curioso-component.component';

describe('CuriosoComponentComponent', () => {
  let component: CuriosoComponentComponent;
  let fixture: ComponentFixture<CuriosoComponentComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CuriosoComponentComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CuriosoComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
